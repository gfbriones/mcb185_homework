#42ntcomp.py by Gennie Fae Briones

import sys
import mcb185 

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    print(name, end = ' ')
    for nt in 'ACGTN':
        print(seq.count(nt) / len(seq), end = ' ') # will count how many specific letters there are in the 'ACGTN' alphabet by seq.count(nt)
    print()

""" 
modifies the program to count 5 nts (ACGTN)
    A = 0
    C = 0
    G = 0
    T = 0
    N = 0
    for nt in seq:
        if nt == 'A': A += 1
        elif nt == 'C': C += 1
        elif nt == 'G': G += 1
        elif nt == 'T': T += 1
        else: N += 1
    print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
 """

'''
list variant

    counts = [0, 0, 0, 0, 0]  
    for nt in seq:
        if nt == 'A': counts[0] += 1
        elif nt == 'C': counts[1] += 1
        elif nt == 'G': counts[2] += 1
        elif nt == 'T': counts[3] += 1
        else: counts[4] += 1
    print(name, end =' ')
    for n in counts: print(n/len(seq), end = ' ')
    print()
'''

'''
indexing with str.find()

    nts = 'ACGTN' #index 
    counts = [0] * len(nts)
    for nt in seq:
        idx = nts.fint(nt)
        counts[idx] += 1
    print(name, end=' ')
    for n in counts: print(n/len(seq), end = ' ')
    print()
'''

'''
counting any letter

    nts = [] #nt empty container
    counts = [] # count empty container
    for nt in seq:
        if nt not in nts:
            nts.append(nt) # adds new nt is found
            counts.append(0) # adds a count when new nt is found 
        idx = nts.index(nt)
        counts[idx] += 1
    print(name)
    for nt, n in zip(nts, counts):
        print(nt, n, n/len(seq))
    print()
'''