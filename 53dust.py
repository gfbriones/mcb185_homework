# 53dust.py by Gennie Fae Briones

import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description = 'DNA entropy filter.')
parser.add_argument('file', type = str, help = 'name of fasta file')
parser.add_argument('-s', '--size', type = int, default=20, help = 'window size [%(default)i]')
parser.add_argument('-e', '--entropy', type = float, default = 1.4, help = 'entropy threshold [%(default).3f]')
parser.add_argument('--lower', action = 'store_true', help='soft mask')
parser.add_argument('--wrap', type = int, default=60)
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)

""" print('first', 'second')
print('first', 'second', sep = '\t', end='\n')
print('first', 'second', end = '\n', sep='\t') """

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


for defline, seq in mcb185.read_fasta(arg.file):
    mask = list(seq)
    for i in range(len(seq) - arg.size + 1):
        wind = seq[i:i+arg.size]
        if entropy(wind) < arg.entropy:
            for j in range(i, i+arg.size):
                if arg.lower:
                    mask[j] = seq[j].lower()
                else: mask[j] = 'N'
    mask = ''.join(mask)
    print('>', defline, sep='')
    
    for i in range(0, len(seq), arg.wrap):
        print(mask[i:i+arg.wrap])            
