#44skew.py by Gennie Fae Briones

import sys
import sequence
import mcb185

w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    initw = seq[:w]
    g = seq[:w].count('G')
    c = seq[:w].count('C')
    print(g ,c)
    for i in range(len(seq) - w):
        off = seq[i]
        on = seq[i+w]
        if off == 'G': g -= 1
        if off == 'C': c -= 1
        if on == 'G': g += 1
        if on == 'C': c += 1
        # print(i, f'g: {g} c:{c}') # check the counts
        if (g + c) != 0:
            print( i ,g + c / len(seq) , (g - c) / (g + c) )
        else: print(i, 0, 0)