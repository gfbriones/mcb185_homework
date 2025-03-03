# 35scoringmatrix.py by Gennie Fae Briones
# write a program that can print out a match-mismatch scoring matrix
import sys

seq = sys.argv[1]
match = int(sys.argv[2])
mismatch = int(sys.argv[3])

header = '  '.join(seq)
print(f'{header:>13}')

for nt1 in range(0, len(seq)):
    row = [seq[nt1]]
    for nt2 in range(0,len(seq)):
        if seq[nt1] == seq[nt2]:
            score = f'+{match}'
        else:
            score = f'{mismatch}'
        row.append(score)
    print(' '.join(row))
