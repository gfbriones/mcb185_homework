# 48transmembrane.py by Gennie Fae Briones

import sys
import mcb185

aas = ['I', 'V', 'L', 'F', 'C', 'M', 'A', 'G', 'T', 'S', 'W', 'Y', 'P', 'H', 'E', 'Q', 'D', 'N', 'K', 'R']

hydro_scores = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

def avg_kd(seq):
    total = 0
    for aa in seq: 
        if aa in aas: 
            total += hydro_scores[aas.index(aa)]
    return total / len(seq)

transmem = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    
    signal = False
    region = False

    N_term = seq[:30]
    pls_m = seq[31:]

    for i in range(len(N_term) - 8 + 1):
        sp = N_term[i:i+8]
        if 'P' in sp: continue
        if avg_kd(sp) >= 2.5:
            signal = True
            break

    for i in range(len(pls_m) - 11 + 1):
        tm_reg = pls_m[i:i+11]
        if 'P' in tm_reg: continue
        if avg_kd(tm_reg) >= 2.0:
            region = True
            break

    if signal and region:
        print(defline)
        transmem += 1
print(transmem)