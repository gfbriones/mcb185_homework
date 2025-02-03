# 12phred.py by Gennie Fae Briones
# Write functions that convert quality value symbols into error rates and vice-versa. 
# The ord() function returns the ASCII value of a letter. The chr() function turns an ASCII value into a letter.

# Demonstrate the functions work by calling them several times. Edge cases should return None.
import math

def char_to_prob(a):
    if ord(a) >= 33 and ord(a) <= 75: # be based on ascii base 33
        q = ord(a) - 33 
        error_rate = 10 ** (q / -10)
        return error_rate
    else: return None 
print(char_to_prob('A'))
print(char_to_prob('T'))
print(char_to_prob('='))

def prob_to_char(a):
    if a <= 0 and a > 1: 
        return None
    p = -10 * math.log10(a)
    q = chr(int(p) + 33)
    if ord(q) >= 33 and ord(q) <= 75:
        return q
    else: return None

print(prob_to_char(0.001))
print(prob_to_char(3))
print(prob_to_char(0.433))
