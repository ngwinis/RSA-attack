from math import isqrt
from Crypto.Util.number import *
from sympy import nextprime

m = bytes_to_long(b'secret_message')

# Tạo khoá
p = getPrime(512)
q = nextprime(p+10**50)
n = p * q
e = 65537
c = pow(m,e,n)

# Các thành phần được tạo từ server
print('-'*20, 'Secret component', '-'*20)
print(f'{m=}\n{p=}\n{q=}')

# Public
print('-'*20, 'Public component', '-'*20)
print(f'{n=}\n{e=}\n{c=}')

# Attack
print('-'*25, 'Attack', '-'*25)
def fermat_factorization(n):
    a = isqrt(n) + 1  # Start from the ceiling of sqrt(n)
    while True:
        b_squared = a * a - n
        b = isqrt(b_squared)
        if b * b == b_squared:
            return (a - b, a + b)
        a += 1

# Find the factors
found_p, found_q = fermat_factorization(n)
print(f"found_p: {found_p}")
print(f"found_q: {found_q}")

phi = (found_p - 1) * (found_q - 1)
d = pow(e, -1, phi)
print(f'message: {long_to_bytes(pow(c,d,n))}')