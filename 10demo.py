# 10demo.py by Gennie Fae Briones

import math

"""
hi teehee
"""
 
print ('hello, again') # greeting

print(1.5e-2)
print(2**3)
print(5%2)
print(5//2)
print(5*(1+2))
print(math.pow(4,5))
print(math.log(3))
print(math.log10(5))

print(0.1 * 1)
print(0.1 * 3)

## pythagoras practice ##
a = 3						# side of triangle
b = 4						# side of triangle 
c = math.sqrt(a**2 + b**2)	#hypotenuse
print(c)
print (type(a), type(b), type(c), sep = ",", end= '!\n')

def pythagoras(a, b):
	c = math.sqrt(a**2 + b ** 2)
	return c

hyp = pythagoras(3,4)
print (hyp)

def pythagoras(a, b):
	return math.sqrt(a**2 + b ** 2) # same thing as def function above 
print(pythagoras(3,4)) # dont need variable hyp 

def pythagoras(a,b): return math.sqrt(a**2 + b**2)

def circle_area(r): return math.pi * (r**2)
def rectangle_area(w,h): return w * h

def triangle_area(w,h): return rectangle_area(w,h) / 2

## convert temp thats in F to C
def temperature(f): return (f-32)*(5/9)
print (temperature(80))

# convert f to c (class Thurs)
def FtoC(f):
    return (f-32)*(5/9)
    
#convert mph to kph
def m2k(m): return m / 0.62
print (m2k(76))

# convert temp in C to F
def temp(c): return (c*(9/5))+32
print (temp(-20))

#Compute the arithmetic mean of 3 numbers
def amean(a, b, c): return (a + b + c)/3
print (amean(3,4,8))

# Compute the geometric mean of 3 numbers
def gmean(a, b, c): return (a*b*c)**(1/3)
print (gmean(3,1,5))

# harmonic mean
def hmean(a, b, c):
    n = 3 
    sum = (1/a) + (1/b) + (1/c)
    return n/sum
print (hmean(5,6,7))

# Compute the distance between 2 points in a graph
def dis(x1, y1, x2, y2):
    x_dis = x2 - x1 
    y_dis = y2 - y1
    return math.sqrt(x_dis ** 2 + y_dis ** 2)
print (dis(1,2,3,4))

s = 'hello world'
print (s, type(s))

a = 2
b = 7
if a == b:
    print ('a equals b')
print (a , b)

def is_even(x):
    if x % 2 == 0: return True
    return False
print(is_even(2))
print(is_even(3))

c = 3 == 3
print(c)
print(type(c))

if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

if a < b: print('a < b')
elif a <= b: print ('a <= b')
elif a == b: print ('this will never be printed!') # will execute ln 112 bcs it will be true

if a < b or a > b: print('all things are equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

## never test for equality with floating numbers! 
a = 0.1 
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

# examine their difference and if its less than some acceptable precision, consider them to be the same
print(abs(a-b))
if abs(a - b) < 1e-19: print ('close enough')
if math.isclose(a, b): print ('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

a = 1
s = 'G'
# if a < s: print('a < s') # will print an error bc ure comparing to int and str

def silly(m, x, b):
    y = m * x + b
print(silly(2, 3, 4))

# write a function that determines if a number is an integer
def is_integer(a): 
    if a % 1 == 0: return True
    return False
print(is_integer(3.2))
print(is_integer(7))
print(is_integer(-3))

# write a function that determines if a number is a valid probability
def is_valid_prob(a):
    if a <= 1 and a >= 0: return True
    return False
print(is_valid_prob(0.3133221))
print(is_valid_prob(5)) 

# write a function that returns the molecular weight of a DNA letter
# if the letter doesn't match any nucleotide, return None

def mw_dna(a):
    if a == 'A': return 'the molecular weight is 313.2 Daltons'
    elif a == 'C': return 'the molecular weight is 289.2 Daltons'
    elif a == 'G': return 'the molecular weight is 329.2 Daltons'
    elif a == 'T': return 'the molecular weight is 304.2 Daltons'
    else: return None 
print(mw_dna('T'))
print(mw_dna('Y')) 

# write a function that returns the complement of a DNA letter, returning None if the letter isn't DNA
def comp_dna(a):
    if a == 'A': print('T')
    elif a == 'C': print('G')
    elif a == 'G': print('C')
    elif a == 'T': print ('A')
    else: return print(None)
comp_dna('A')
comp_dna('X')

# Write a function that returns the maximum of 3 numbers. 
# the function takes 3 input parameters and returns the single largest one

def max3(a, b, c):
    if a >= b and a >= c: return a
    elif b >= a and b >= c: return b
    else: return c
print(max3(-4,-8,-1))
print(max3(5,6,44))

# Given values for true positives, false positives, true negatives, and false negatives
# write functions that return sensitivity, specificity, and F1 score

def stat(tp, fp, tn, fn): 
    def sen(tp, fn):
        if tp + fn == 0: return 0
        return tp / (tp + fn)

    def spec(tn, fp):
        if tn + fp == 0: return 0
        return tn / (tn + fp)

    def f1(tp, fp, fn):
        if tp + fp + fn == 0: return 0
        return tp / (tp + ((1/2) * (fp + fn)))
    print ((sen(tp, fn)), spec(tn, fp), f1(tp, fp, fn))
print(stat(4,5,3,8))

# Write a function that returns the Shannon entropy for nucleotide counts A, C, G, T. 
# It should work even in the case where there are zero counts for one or more letters.

def shannon(a, c, g, t):
    total = a + c + g + t
    if total == 0: return 0

    if a > 0: 
        a_prob = a / total
        a_entropy = a_prob * (-math.log2(a_prob))
    if a_entropy == 0: return 0
    if c > 0:
        c_prob = c / total
        c_entropy = c_prob * (-math.log2(c_prob))
    if c_entropy == 0: return 0
    if g > 0: 
        g_prob = g / total
        g_entropy = g_prob * (-math.log2(g_prob))
    if g_entropy == 0: return 0
    if t > 0:
        t_prob = t / total
        t_entropy = t_prob * (-math.log2(t_prob))
    if t_entropy == 0: return 0

    total_entropy = a_entropy + c_entropy + g_entropy + t_entropy
    return total_entropy
print(shannon(5, 4, 2, 6))

    


    



   