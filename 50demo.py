# 50demo.py by Gennie Fae Briones

'''
Sets 
- mutable chara, all of the elements are unique and elements are NOT ordered
'''

s = {'A', 'C', 'G'}
print(s) # prints in diff order 

# add() - add items to set
s.add('T')
print(s)

s.add('A') # adding the same element (A) doesnt do anything
print(s)

#print(s[2]) > error bcs it doesnt have order 

'''
Dictionaries
- like list
- indices are strings instead of numbers 

list[0] - 0 is a numberic index 
dict['hey'] - 'hey' is a string index 

- unlike like indices, no append() for dictionaries
- each item in dict exists as a key:value pair 
    - key = string in square brackets (ex: 'hey' above)
    - value = anything u can put in a variable 
'''

# empty dict is created either with empty braces or dict() function
d = {}
d = dict()

# to make a dict with predefined items, use curly braces and key:values pairs
d = {'dog': 'woof', 'cat': 'meow'}
print(d)
# both dict and sets are displayed with curly brackets 
    # dict - key:value pairs
    # sets - only values

# to access items, use square brackets 
print(d['cat']) # prints meow

# to add new items to a dict, assign a new key:value pair 
d['pig'] = 'oink'
print(d)

# to change the value of an item, access it with its key 
d['cat'] = 'mew'
print(d)

# to delete an item, use del
del d['cat']
print(d)

# if you try to access a key that doesnt exist, you get an error 
# print(d['rat'])

# to check if a key exist: use the keyword in 
if 'dog' in d: print(d['dog'])

'''
Interation for Dictionary
'''
# - standard for loop: iterates over the keys in order in which they were created, 
    #to get specific element, use the key as an index to the dictionary 
for key in d: print(f'{key} says {d[key]}')

# - most common way to iterate through a dict is with dict.items()
for k, v in d.items(): print(k, 'says', v)

# should always unpack ur tuples
for thing in d.items(): print(thing[0], thing[1])

# if want just keys: dict.keys()
# if want just values: dict.values()
# if want these as actual lists: coerce them with list()

print(d.keys(), d.values(), list(d.values()))

#counts nts in seqs 
seq = 'ACGTTGAATT'
count = {}
for nt in seq: 
    if nt not in count: count[nt] = 0
    count[nt] += 1

'''
Sorting dict by keys or values

- pipe the program output through Linux sort

python3 51countgff.py ecoli.gff.gz | sort 
    > sorts output by the feature name 

python3 51countgff.py ecoli.gff.gz | sort -n -k 2
    > sorts the second column (-k 2) numerically (-n)

python3 51countgff.py ecoli.gff.gz | sort -nk2
    > same thing as above 
'''
# want to sort to occur inside python? 
# use sorted() to sort the keys of count
for k in sorted(count): print(k, count[k])

# sorted() function needs a list of things to sort 
# default: keys 
# want to sort items based on values > send sorted() the values of the items 
'''
for k, v in sorted(count.items(), keys = lambda item: item[1]):
    print(k ,v)


Lambda functions - tiny anonymous functions
- lambda function above reads the tuple item and returns the 2nd element item[1] as the return value 
'''

def by_value(tuple):
    return tuple[1]

for k, v in sorted(count.items(), key = by_value):
    print(k ,v)

'''
K-mers
'''

import itertools
for nts in itertools.product('ACGT', repeat = 2):
    print(nts)

'''
Argparse
- usage statements and command line options 
'''