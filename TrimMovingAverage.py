###############################################################################
# Python Script to Trim Based on Moving Average
###############################################################################
# Written by Mario Muscarella
# Last Update 22 Mar 2019

# Directions:

from Bio import SeqIO
import sys
import glob
import numpy as numpy
#import MovingAverage as MovingAverage

window_size = 10
qual_cutoff = 30

def movingaverage(data_in, window_size):
	window = numpy.ones(int(window_size))/float(window_size)
	return numpy.convolve(data_in, window, 'same')

files = sorted(glob.glob("*.qual"))

for x in files:
	sample_qual = SeqIO.read(x, "qual")
	sample_seq = SeqIO.read(sample_qual.id+".fasta", "fasta")
	sample_qual_score = sample_qual.letter_annotations["phred_quality"]
	sample_qual_MA = numpy.array(movingaverage(sample_qual_score, window_size))
	if numpy.max(sample_qual_MA) > qual_cutoff:
		qual_above = list(numpy.where(sample_qual_MA > qual_cutoff))[0]
		sample_qual_min = numpy.min(qual_above)
		sample_qual_max = numpy.max(qual_above)
		sample_qual_trim = sample_qual[sample_qual_min:sample_qual_max]
		sample_seq_trim = sample_seq[sample_qual_min:sample_qual_max]
		SeqIO.write(sample_qual_trim, sample_qual.id+".trim.qual", "qual")
		SeqIO.write(sample_seq_trim, sample_seq.id+".trim.fasta", "fasta")
		print "trimmed fasta and qual file created for %s" % sample_qual.id
	else:
		print "the maximum quality score for %s is below the cutoff" % sample_qual.id
