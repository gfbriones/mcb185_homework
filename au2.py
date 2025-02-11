# au2.py by Gennie Fae Briones
# 
def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

for i in range(51, 0, -2):
    if is_prime(i):
        print(str(i)+"*")
    else: print(i)