# 47cdsfinder.py by Gennie Fae Briones

import sys
import mcb185
import sequence


filename = sys.argv[1]
min_aa_len = int(sys.argv[2])

protein_count = 0

for defline, seq in mcb185.read_fasta(filename):
    # get defline 
    defline = defline.split()
    new_def = defline[0]

    # get revcomp of seq
    revcomp = sequence.revcomp(seq) 

    frames = [seq, seq[1:], seq[2:], revcomp, revcomp[1:], revcomp[2:]]

    for frame_ind, frame in enumerate(frames):
        trans_seq = mcb185.translate(frame)

    # check for protein sequence thats minimum of 100 aas long 
        proteins = [] # empty list for the proteins that start with M, end with * (min: 100 long)
        in_orf = False # tracks if we're inside in the ORF 

        for aa in trans_seq:
            if aa == 'M':
                proteins = ['M']
                in_orf = True
            elif aa == '*' and in_orf:
                proteins.append('*')
                
                if len(proteins) >= min_aa_len:
                    orf_seq = ''.join(proteins)

                    print(f'>{new_def}-prot-{protein_count}')
                    print(orf_seq)
            
                    protein_count += 1
    
                in_orf = False
            elif in_orf: 
                proteins.append(aa)
