#!/usr/bin/env python

import sys
from collections import Counter
from readfq import readfq

IUPAC_BASES = "ACGTRYSWKMBDHVN-." # nucleotide abbrevs as global variable

counts = Counter() # initialize counter; accessible as dictionary

for name, seq, qual in readfq(sys.stdin):
	counts.update(seq.upper()) # for each sequence, adds bases into counter

for base in IUPAC_BASES:
	print base + '\t' + str(counts[base]) # accessing the count dictionary here