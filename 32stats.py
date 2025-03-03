# 32stats.py by Gennie Fae Briones

# program that reports descriptive stats for numbers on the command line
# should report: 
    # number of values
    # minimum and maximum values
    # mean and std 
    # median 
import sys
import math

vals = []

# add them into a list(vals)
for arg in sys.argv[1:]:
    f = float(arg)
    vals.append(f)

# number of values in the list
count = len(vals)
print(f'Number of Values: {count}')

# minimum and maximum values
min = vals[0]
max = vals[0]
for val in vals:
    if val < min: min = val
    if val > max: max = val
print(f'Min: {min}')
print(f'Max: {max}')

# mean 
total = 0
for val in vals: total += val 
mean = total / count
print(f'Mean: {mean}')

# std
sd2 = 0
for val in vals:
    sd2 += (val - mean) ** 2
    std = math.sqrt(sd2 / count)
print(f'Standard Deviation: {std:.4f}')

# median
vals.sort()
if count % 2 == 0: 
    med1 = vals[count//2]
    med2 = vals[count//2 -1]
    med = (med1 + med2) / 2
else: med = vals[count// 2] 
print(f'Median: {med}')

#N50
n50half = total / 2
num50sum = 0 
for val in vals: 
    num50sum += val
    if num50sum >= n50half: 
        n50 = val
        break
print(f'N50: {n50}')