t = 1, 2 # this is a tuple
print(t)
print(type(t))

person = 'Steven', 21, 57891.50 # person, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2): 
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
print(m)
print(m[0], m[1]) # unpacks m which has x, y tuple 
mx, my = midpoint(1, 2, 3, 4)
print (mx, my)

# while loop: followed by an expression that is true or false, then indented 

# while True: 
    # print('hello') # loop of hello will never stop !!

i = 0 
while True:
    i += 1 # adds one per loop 
    print('hey', i)
    if i == 3: break # loop breaks when it hits 3 times 

i = 0
while i < 3: # better to have some kind of condition when its not true no more 
    i += 1
    print('hey', i)

i = 0 
while i < 10: # modified code starts at 1, ends before 10, skips by 3
    print(i)
    i += 3
print('the final value of i is', i)

for i in range(1, 10, 3): # for loop with range() that starts at 1, ends before 10, adds by 3 
    print(i)

for i in range(5): # ends before 5 as default increment is 1 and for loops starts at 0 
    print(i)

# same codes as above 
for i in range(0, 5, 1): print(i)
for i in range(0, 5): print(i)

basket = 'milk', 'eggs', 'bread'
for thing in basket: # for loop goes through each thing in basket tuple 
    print(thing)

for i in range(len(basket)): # for loop uses range and len() -> returns the number of items in basket
    print(basket[i])

for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else: print(i, 'is odd')
 

## practice problems

# Write a function that calculates the triangular number. This is the sum of numbers from 1 to n.
def tri(n): 
    for i in range(1,n):
        n += i
        i += 1
    return n
print(tri(5))

# Write a function that calculates the factorial of a number.
def fact(n):
    if n == 0: return 1
    for i in range(1,n):
        n *= i 
        i += 1
    return n
print(fact(3))

# Write a function that computes the Poisson probability 
# of k events occurring with an expectation of n: n^k e^-n / k!
import math

def poisson(n, k):
    poisson_prob = (n ** k) * (math.e ** (-n)) / fact(k)
    return poisson_prob
print(poisson(4, 2))

# Write a function that solves "n choose k": n! / k!(n - k)!

def nck(n ,k):
    choose = fact(n) / (fact(k) * fact(n - k))
    return choose
print(nck(7, 5))

# Write a function that estimates Euler's number: e (2.71828...). 
# This can be computed as the infinite sum of 1/n!. Choose a finite number of iterations.


def euler(n): 
    e = 0
    for i in range(n):
        e = e + 1/fact(i)
    return e
print(euler(100))

# Write a function to determine if a number is prime.

def is_prime(n):
    for den in range(2, n//2 + 1):
        if n % den == 0: 
            return False
    return True
print(is_prime(17))
print(is_prime(27))

# Write a function that estimates Pi (3.14159...) using the Nilakantha series. 
# Again, choose a finite limit. Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...

def nilakantha(limit):
    sign = -1
    pi = 3 
    for i in range(1, limit + 1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi

# monty pi-thon 

import random

x = random.random()
y = random.random()

print(x, y)

dis = (x ** 2 + y ** 2) ** (0.5) 

in_circle = dis <= 1

pi_appr = 0
ins = 0 
out = 0


while True: 
    x = random.random()
    y = random.random()
    dis = (x ** 2 + y ** 2) ** (0.5)
    in_circle = dis <= 1
    if in_circle: 
        ins += 1
    else: out += 1
    pi_appr = ins / (ins + out) * 4
    print(pi_appr)
