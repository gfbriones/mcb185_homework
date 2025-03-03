import random
import math

# string = container that holds letters, numbers, punctuations, and other symbols

s = 'hello world'
print(s)

s1 = 'hey "dude"' #double qoute if want qoute inside string
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')
# backslash(\) = special characters

"""
String operators

= -> assigment, ex: s = 'hello'
+ -> concatenation, ex: s = 'hello' + 'world'
* -> repetition, ex: polyA = 'A' * 100
> -> comparsion, ex: if s1 > s2
< -> comparsion, ex: if s1 < s2
== -> comparsion, ex: s1 == s2

+ comparsions with strings are compared by their ASCII values
    - 'A' is less than 'B'
    - 'B' is less than 'a' > all capitals are less than lowercase
    - '1' is less than '10' ('a' is less than 'ace')
    - '2' is greater than '1000' ('b' is greater than 'ant')
"""

##string functions

#len() = returns length of string
#chr() = returns character whose ASCII value is n
#ord() = returns the ASCII value of character c

## method syntax 
'''
s.count(s1) = number of occurences of s1 in s
s.endswith(s1) = true if s ends with s1
s.startswith(s1) = true if s starts with s1
s.upper() = uppercase version of s
s.lower() = lowercase ver of s
s.rstrip() = strip chara from the right (spaces by default)
s.replace(a, b) = convert substring a to b
'''

print(s.upper())
print(s)

print(s.replace('o', ' '))
print(s.replace('o', '').replace('r', 'i'))

#format 
'''
f-strings - modern and best way
str.format() - older method 
printf-style - something that looks like printf() from C

to create a f-string: precede a string with f  
    - inside f-string, anything in curly brackets = interpolated
    - inside curly brackets
        - f for fixed pt
        - e for exponent notation
        - < ^ > for left, center, right justify
'''

print(f'{math.pi}')
print(f'{math.pi:.3f}') # 3 fixed digits after decimal 
print(f'{1e6 * math.pi:e}') # exponent notation
print(f'{"hello world":>20}') # right justify with space filter
print(f'{"hello world":>.20}') # right justify with dot filter
print(f'{20:<10} {10}') # left justify 

# str.format():
    # empty curly braces, filled with parameters of str.format() parameters
print('%s %.3f' % ('printf', math.pi))

# indexes - position of chara in string

seq = 'GAATTC'
print(seq[0], seq[1]) # prints out G A

print(seq[-1]) # indexes can be neg, counts backwards, prints out C

for nt in seq: # iterate through each chara in seq string
    print(nt, end = ' ')
print()

for i in range(len(seq)): # iterates thru letters by their indices, range = generate indices and len = set the limit
    print(i, seq[i])

'''
Slices
    - subset of a container
    - slice operator uses a pair of square brackets with : inside
    - works similar like range() where they take initial pos and end-before limit
'''

s = 'ABCDEFGHIJ'
print(s[0:5]) # prints first 5 letters of string, starts at pos 0 and ends before 5 (A-E)

#similar to range() function, slices can also have step sizes, default is 1
print(s[0:8:2])

# shortcuts - can omit either the init val (replaced by 0) or final val (len of string)
print(s[0:5], s[:5]) #both ABCDE
print(s[5:len(s)], s[5:]) #both FGHIJ

#s[0] is the same thing as s[0:1], indexes single element
#s = s[0:len(s)], s[::], s[::1], sets the bounds of the slice to the whole string

print(s, s[::], s[::1], s[::-1]) #s[::-1] makes string backwards

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3): #slices a string into condons
    codon = dna[i:i+3] #starts at i and ends before i+3
    print(i, codon)

'''
Tuples
- container that holds multiple values
- generally constructed with comma-separated values, (in parentheses)
'''

tax = ('Homo', 'sapiens', 9606) # create tuple 
print(tax) # note the parentheses in output 

#tuples and strings = immutable, cannot change their contents by poking at indices 

# s[0] = 'C' 
# tax[0] = 'human' 
    # will have errors in outputs! 

#tuples = linear containers of values, can be indexed and sliced using same syntax
print(tax[0]) # index
print(tax[::-1]) # slice

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i]) # will provide both indices and values

# enumerate() creates a tuple containing the index and value in separate named variables
for i, nt in enumerate(nts):
    print(i, nt)

#zip() allows to retrieve an element from each container and return them you into a tuple
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for nt, name in zip(nts, names):
    print(nt, name)

#can even do both!
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)

# Lists
# - similar to tuple, contstructed with [] and contents are mutable

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

# - list.append(): elements can be added to the end of the list  
nts.append('C')
print(nts)

# - list.pop(): remove elements from end of the list 
last = nts.pop()
print(last)

# - list.sort(): sorts list, all of the elements in list MUST have similar types, can sort mix of ints and floats, not with strings
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

# - if make a new vara to existing list = NOT A COPY, just another name for same list
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# - list.copy(): makes a copy, shallow copy (multi-dimen lists and other complex data structures are not fully copied)

# - list(): creates empty lists
items = list()
print(items)
items.append('eggs')
print(items)

# can create emtpy lists with []
stuff = []
stuff.append(3)
print(stuff)

# - list(): also can forces other iterables into lists 
alph = 'ABCDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

#- str.split(): splits strings into lists of strings, useful for segmenting words, default: any n of spaces
text = 'good day                to you'
words = text.split()
print(words)

#tsv and csv data - split on \t or comma 
line = '1.41,2.72,3.14'
print(line.split(','))

# lists can be turned into strings by joining them with a delimiter, delim can be nothing
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

#Searching 
# - to search for items in containers, can use in, find(), and index()

# in: reads particularly well in conditional statements 
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

# index(): returns the index of first element it finds, if cant find a matching item, function throws error 
print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z')) #error!

# find(): returns index of first element it finds or a -1 if it cant be found, useful for strings!! not tuples or lists
print('find G?', alph.find('G')) # returns what pos the G is at (6th pos)
print('find Z?', alph.find('Z'))

## PRACT PROBS

# minimum value of list
def min(vals):
    mini = vals[0]
    for val in vals[1:]:
        if val < mini: mini = val
    return mini

print(min([4,2,5,6]))

#both min and max of a list
def minmax(vals):
    mini = vals[0]
    max = vals[0]
    for val in vals[1:]:
        if val < mini: mini = val
        if val > max: max = val
    return mini, max

print(minmax([4,5,7,2,8,9]))

# returns the mean of values in a list
def mean(vals):
    sum = 0
    for val in vals: sum += val
    return sum / len(vals)
print(mean([4,5,1]))

# entropy of prob distribution
def entropy(probs):
    h = 0
    for prob in probs:
        h -= prob * math.log2(prob)
    return h
print(entropy([0.2, 0.6, 0.4]))

# kullback-leibler distance
def kldis(P, Q):
    kl = 0
    for p,q in zip(P, Q):
        kl += p * math.log2(p/q)
    return kl

p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(kldis(p1, p2))

'''
Common Line Data
'''

# sys.argv - complete list of words on the command line
#   - sys.argc[0] = name of program, sys.argv[1] = first argument

import sys
print(sys.argv)

#   - there will be [] bcs sys.argv is a list
#   - numeric vals have 'quotes' around them bcs theyre strings

## converting types
i = int('42') # int for whole numbers 
x = float('0.61803') #float for decimals, fractions
print(i * x)

# if u run into an error and want to provide a custom message, use sys.exit()

'''
Pairwise Comparison

3 ways to perform all vs all comparsions
- all combinations
- unique pairings allowing self-comparsions (half matrix w/ diagonal)
- unique pairings disallowing self-comparsions (half matrix w/o diagonal)

for i in range(0, len(list)):
    for j in range(X, len(list)):

X can be change depending on the 3 diff kindsd of pairwise comparsions 
    X = 0: all combos 
    X = i: half-matrix w/ diagonal
    X = i+1: half-matrix w/o diagonal
'''


## Assessment Examples

'''
1. what does this mean:
print('-'.join(list('ABCDE'))[3:6])

> will print out the characters in the 'ABCDE' list will be separated by dashes
starting from the 3rd chara (-) and ends PRIOR the 6th chara (D) 

> so the output will be: -C-

2. add the N50 calculation to 32stats.py program

3. given a nucleotide sequence, create an output that shows position, frame, and codon separated by tabs
'''



