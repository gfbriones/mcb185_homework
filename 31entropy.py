# 31entropy.py by Gennie Fae Briones

import sys
import math

probs = []
for arg in sys.argv[1:]:
    f = float(arg)
    if f <= 0 or f >= 1: sys.exit('error: not a probability')
    probs.append(f)

total = 0
for prob in probs: total += prob
if not math.isclose(total, 1.0): sys.exit('error: must sum to 1.0')

h = 0
for prob in probs:
    h -= prob * math.log2(probs)

print(f'{h:.4f}')