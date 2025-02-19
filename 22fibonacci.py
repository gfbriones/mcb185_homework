# 22fibonacci.py by Gennie Fae Briones
# 
# write a program that reports the first 10 numbers from 
# the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

num1 = 0
num2 = 1
print(num1)
print(num2)

for i in range(8):
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3


