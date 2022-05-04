# Sanger Sequencing Scripts

The scripts included in this repo are to be used to call bases and quality trim sequences from raw AB1 files.

Last Update 2/May/2022

## Contents (in bin):

1. MergeSeqs.py - python MergeSeqs.py (input type) (output name); used to merge multiple files into a multifile. This works for both '.fasta' and '.qual' files. Note: input type is the file extension and is used to designate the file type.
2. MovingAverage.py - python script to calculate moving average; called from other scripts; now included in TrimMovingAverage.py
3. ReadAB1.py - python script to convert .ab1 to .fasta and .qual using BioPython
4. TrimMovingAverage.py - python script to trim based on moving average; defaults: window_size = 10, qual_cutoff = 30
5. TrimPositions.py - python script to trim based on designated start and end positions
6. CheckLength.py -

## How To Use These Scripts:

+ When you submit samples for Sanger Sequencing you can get back processed sequence files ('.fasta' or '.fa'), but these may or may not have been quality filtered to a satisfactory standard. Instead, I recommend manually filtering the raw data ('.ab1'). You cannot open these files because they are binary. However, these scripts will allow you to process the raw files and generate quality filtered sequence reads.

+ Use ReadAB1.py to convert '.ab1' file to '.fasta'. and '.qual' files. Run function from within the folder containing the '.ab1' files
    Usage: python ~/Github/Sanger_16S/bin/ReadAB1.py

+ Use TrimMovingAverage.py to trim the raw '.fasta' files based on a moving average quality score. The quality score is taken from the corresponding '.qual' file. This script is designed to trim all corresponding '.qual' and '.fasta' files.
    Usage: python ~/Github/Sanger_16S/bin/TrimMovingAverage.py

+ Merge fasta and qual files into corresponding multifiles: multifasta '.fasta' and multiqual '.qual'
    Usage: python ~/Github/Sanger_16S/bin/MergeSeqs.py "trim.fasta" "fasta" [output_name.fasta]
           python ~/Github/Sanger_16S/bin/MergeSeqs.py "trim.qual" "qual" [output_name.qual]

+ Check results by comparing length using CheckLength.py
    Usage: 3 ~/Github/Sanger_16S/bin/CheckLength.py [input file]


## Example Pipeline:
(note: python3 just calls python 3.9 on my system)
+ python3 ~/Github/Sanger_16S/bin/bin/ReadAB1.py 
+ python3 ~/Github/Sanger_16S/bin/bin/TrimMovingAverage.py
+ python3 ~/Github/Sanger_16S/bin/bin/MergeSeqs.py "trim.fasta" "fasta" "PhosTraits.fasta"
+ python3 ~/Github/Sanger_16S/bin/bin/MergeSeqs.py "[1-2].fasta" "fasta" "PhosTraits.raw.fasta"
+ python3 ~/Github/Sanger_16S/bin/bin/CheckLength.py PhosTraits.fasta
+ python3 ~/Github/Sanger_16S/bin/bin/CheckLength.py PhosTraits.raw.fasta

## Dependencies:
+ Python 2.7 or later
    Python Packages: BioPython, Numpy

## Last Updates
+ 2022: Convert to Python 3.9

## Contributors:
[Mario Muscarella](http://muscarellalab.github.io/): Principle Investigator. Assistant Professor of Microbiology at the University of Alaska Fairbanks.

[Amanda Stromecki](https://github.com/astromecki): Research Professional at University of Alaska Fairbanks.
