from sympy import isprime, mod_inverse
from Crypto.Util.number import *

m = bytes_to_long(b'secret_message')
# Tạo khoá
p, q = getPrime(512), getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)
e = 11
d = pow(e, -1, phi)
c = pow(m,e,n)

# Các thành phần được tạo từ server
print('-'*20, 'Secret component', '-'*20)
print(f'{m=}\n{p=}\n{q=}')
print(f"Khóa riêng thực tế d: {d}")

# Public
print('-'*20, 'Public component', '-'*20)
print(f'{n=}\n{e=}\n{c=}')

# Attack
print('-'*25, 'Attack', '-'*25)

for i in range(1, e):
    d_i = (i * n + 1) // e  
    print(f"Giá trị xấp xỉ của d khi i={i}: {d_i}")
