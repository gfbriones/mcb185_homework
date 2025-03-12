# 46dust.py by Gennie Fae Briones

import sys
import mcb185
import math

filename = sys.argv[1]
w = int(sys.argv[2])
entropy_thres = float(sys.argv[3])


def entropy(wind):
    a = wind.count('A')/len(wind)
    c = wind.count('C')/len(wind)
    g = wind.count('G')/len(wind)
    t = wind.count('T')/len(wind)
    h = 0
    if a != 0: h += a * math.log2(a)
    if c != 0: h += c * math.log2(c)
    if g != 0: h += g * math.log2(g)
    if t != 0: h += t * math.log2(t)
    return -h


for defline, seq in mcb185.read_fasta(filename):
    mask = list(seq)
    for i in range(len(seq) - w + 1):
        wind = seq[i:i+w]
        if entropy(wind) < entropy_thres:
            for j in range(i, i+w):
                mask[j] = 'N'
    
    print('>', defline, sep='')
    mask = ''.join(mask)
    for i in range(0, len(seq), 60):
        print(mask[i:i+60])