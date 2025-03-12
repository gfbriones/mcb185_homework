# 52kmercount.py by Gennie Fae Briones

import sys
import mcb185

k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for i in range(len(seq) -k +1):
        kmer = seq[i:i+k]
        if kmer not in kcount: kcount[kmer] = 0
        kcount[kmer] += 1
for kmer, n in kcount.items(): print(kmer, n)

import itertools
for nts in itertools.product('ACGT', repeat = k):
    kmer = ''.join(nts) # joints tuple nts into a string so can use it to index our dict 
    if kmer in kcount: print(kmer, kcount[kmer])
    else: print(kmer, 0) # any kmers that arent found will be reported with a 0 count 