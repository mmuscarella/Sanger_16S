###############################################################################
# Python Script to Modify Entry Length if Multi Fasta File
###############################################################################
# Written by Mario Muscarella
# Last Update 22 Mar 2018

# Directions:
#  use the following command: > python FormatLong.py [input file] [output file]
import sys
import glob
from Bio import SeqIO

input = sys.argv[1]
output = sys.argv[2]

records = list(SeqIO.parse(input, "fasta"))
SeqIO.write(records, output, "fasta-2line")

print "%i sequences changed to long format" % len(records)
