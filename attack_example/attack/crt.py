from Crypto.Util.number import *
from sympy import root

p1=10086822263673640087
q1=14616807228050434831
p2=14347620969203651177
q2=16538296571908278413
p3=16618067254672148203
q3=14799146539459237073
n1=p1*q1
n2=p2*q2
n3=p3*q3
print(f'{n1=}\n{n2=}\n{n3=}')

e=3
print(f'{e=}')

m = bytes_to_long(b'secret_message')

c1 = pow(m,e,n1)
c2 = pow(m,e,n2)
c3 = pow(m,e,n3)
print(f'{c1=}\n{c2=}\n{c3=}')

N = n1*n2*n3
N1 = N//n1
N2 = N//n2
N3 = N//n3
x = (c1*N1*pow(N1, -1, n1) + c2*N2*pow(N2, -1, n2) + c3*N3*pow(N3, -1, n3)) % N

print(f'message: {long_to_bytes(root(x,e))}')