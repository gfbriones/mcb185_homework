# 11oligo.py by Gennie Fae Briones
# Write a function that returns the oligo melting temperature 
# given the number of As, Cs, Gs, and Ts in the oligo. Use these two methods.

# 1. For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
# 2. For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C) 

def tm(a, c, g, t):
    total_nt = a + c + g + t
    if total_nt <= 13: 
        tm = (a + t) * 2 + (g + c) * 4
        return tm
    else: 
        tm = 64.9 + 41*(g + c - 16.4) / (total_nt)
        return tm
    
print (tm(5, 7, 3, 4))
print(tm(3, 3, 3, 4))
print(tm(3, 6, 1, 4))
print(tm(9, 2, 3, 7))
