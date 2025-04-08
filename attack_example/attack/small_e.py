from Crypto.Util.number import *
from sympy import root

m = bytes_to_long(b'secret')
# Tạo khoá
p, q = getPrime(512), getPrime(512)
n = p*q
e = 3
c = pow(m,e,n)

# Các thành phần được tạo từ server
print('-'*20, 'Secret component', '-'*20)
print(f'{m=}\n{p=}\n{q=}')

# Public
print('-'*20, 'Public component', '-'*20)
print(f'{n=}\n{e=}\n{c=}')

# Attack
print('-'*25, 'Attack', '-'*25)
print(f'decrypted_message = {long_to_bytes(root(c,e)).decode()}')