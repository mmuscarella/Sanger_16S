###############################################################################
# Python Script to Combine Fasta or Qual Files Using BioPython
###############################################################################
# Written by Mario Muscarella
# Last Update 25 Apr 2013

# Directions:
#  use the following command: > python MergeSeqs.py (input type) (output name)
import sys
import glob
from Bio import SeqIO
 
input_name = sys.argv[1]
input = sys.argv[2]
output = sys.argv[3]

entries = []
 
files = glob.glob("*."+input_name)
for file in files:
	temp = SeqIO.read(file, input)
	entries.append(temp)
	SeqIO.write(entries, output, input)
print "%i files combined" % len(entries)
print "Output written to %s" % output