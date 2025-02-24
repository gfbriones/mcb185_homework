# 23triples.py by Gennie Fae Briones
# 
# Write a program that finds all Pythagorean triples for triangles with sides a and b less than 100. 
# For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2

import math

limit = 100

for a in range (1 ,limit):
    for b in range(a + 1, limit):
        c = math.sqrt(a**2 + b**2)
        if c % 1 == 0:
            print(a,b,c)