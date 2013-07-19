###############################################################################
# Python Script to Convert .ab1 to .fasta and .qual Using BioPython
###############################################################################
# Written by Mario Muscarella
# Last Update 25 Apr 2013

import glob
files = glob.glob("*.ab1")
#names= []
#for x in files:
#	tempname = (x).split(".")[0]
#	names.append(tempname)

from Bio import SeqIO
for x in files:
	sample_seq = SeqIO.read(x, "abi")
	sample_seq.id = sample_seq.name
	SeqIO.write(sample_seq, sample_seq.id+".fasta", "fasta")
	SeqIO.write(sample_seq, sample_seq.id+".qual", "qual")
	print "fasta and qual file created for %s" % sample_seq.id
