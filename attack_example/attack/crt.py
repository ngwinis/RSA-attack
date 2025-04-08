from Crypto.Util.number import *
from sympy import *

m = bytes_to_long(b'secret_message')

# Tạo khoá
p1, q1 = getPrime(512), getPrime(512)
p2, q2 = getPrime(512), getPrime(512)
p3, q3 = getPrime(512), getPrime(512)
e = 3
n1=p1*q1
n2=p2*q2
n3=p3*q3
c1 = pow(m,e,n1)
c2 = pow(m,e,n2)
c3 = pow(m,e,n3)

# Các thành phần được tạo từ server
print('-'*20, 'Secret component', '-'*20)
print(f'{m=}\n{p1=}\n{q1=}')
print(f'{p2=}\n{q2=}')
print(f'{p3=}\n{q3=}')

# Public
print('-'*20, 'Public component', '-'*20)
print(f'{n1=}\n{n2=}\n{n3=}')
print(f'{e=}')
print(f'{c1=}\n{c2=}\n{c3=}')

# Attack
print('-'*25, 'Attack', '-'*25)
N = n1*n2*n3
N1 = N//n1
N2 = N//n2
N3 = N//n3
x = (c1*N1*pow(N1, -1, n1) + c2*N2*pow(N2, -1, n2) + c3*N3*pow(N3, -1, n3)) % N

print(f'message: {long_to_bytes(root(x,e))}')
