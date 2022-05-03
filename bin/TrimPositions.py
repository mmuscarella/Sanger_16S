###############################################################################
# Python Script to Trim Based on designated start and end
###############################################################################
# Written by Mario Muscarella
# Last Update 10 May 2013

# Directions:

from Bio import SeqIO
import sys
import glob
from Bio.SeqIO.FastaIO import FastaWriter

# change these numbers
start = 1130 
end = 42988

def trim_positions(records, start, end):
	for record in records:
		yield record[start:end]

#files = glob.glob("*.align")
file = "HMWF.align"

original_seqs = SeqIO.parse(file, "fasta")
trimmed_seqs = trim_positions(original_seqs, start, end)
output_handle = open(file+".trim.fasta", "w")
count = FastaWriter(output_handle, wrap=0).write_file(trimmed_seqs)
output_handle.close()
print "Trimmed %i reads" % count

