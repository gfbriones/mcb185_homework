#45colorname.py by Gennie Fae Briones
# write a program that provides the closest official color name given some red, green, and blue values

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
ls_colors = [R,G,B]


def dtc(P,Q):
    d = 0
    for p,q in zip(P, Q):
        p = int(p)
        q = int(q)
        d += abs(p-q)
    return d

min = 0 #to track minimum values

with open(colorfile) as fp: 
    for line in fp:
        line = line.split()
        color_code = line[2]
        color_code = color_code.split(',')
        diff = dtc(color_code, ls_colors)
        if diff < min or min == 0:
            min = diff
            color = line[0]

print(color)