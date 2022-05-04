###############################################################################
# Python Script to Check Sequence Lengths in MultiFastaFile
###############################################################################
# Written by Mario Muscarella
# Last Update 22 Mar 2018

# Directions:
#  use the following command: > python CheckLength.py (input file)
import sys
import glob
from Bio import SeqIO

input = sys.argv[1]

for seq_record in SeqIO.parse(input, "fasta"):
    sample = seq_record.id
    length =  len(seq_record)

    print("Sequence %s is %s bp long" % (sample, length))
