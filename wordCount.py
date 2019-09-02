#! /usr/bin/env python3

import sys   # command line arguments
import re    # regular expression tools
import os    # checking if files exist

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output text file>")
    exit()
    
inputFileName= sys.argv[1]
outputFileName= sys.argv[2]

# make sure text files exist
if not os.path.exists(inputFileName):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()


# master dictionary
master = {}
            
# read the text file to count
with open(inputFileName, 'r') as inputFile:  # r is read only mode
    for line in inputFile:
        # Get rid of newline characters
        line = line.strip()
        # Make all lowercase
        line = line.lower()
        # split line on whitespace and punctuation
        check = re.split('[ \t]', line)
        for word in check:
            if not word in master:
                master[word] = 1 #Added word to dictionary
            else:
                 master[word] = master[word] + 1 # increment count for the word
master = sorted(master.items())

# Write to output file
with open(outputFileName, 'w') as outputFile:
    for x in master:
        outputFile.write (x + " " + master[x])
        
