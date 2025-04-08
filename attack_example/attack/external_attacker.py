from Crypto.Util.number import *
from sympy import gcdex

m = bytes_to_long(b'secret_message')

# Tạo khoá
p, q = getPrime(512), getPrime(512)
n = p * q
e1, e2 = 65537, 72547
c1, c2 = pow(m, e1, n), pow(m, e2, n)

# Các thành phần được tạo từ server
print('-'*20, 'Secret component', '-'*20)
print(f'{m=}\n{p=}\n{q=}')

# Public key
print('-'*20, 'Public component', '-'*20)
print(f'{n=}\n{e1=}\n{e2=}\n{c1=}\n{c2=}')

# Tìm u, v sao cho e1*u + e2*v = 1
print('-'*25, 'Attack', '-'*25)
u, v, _ = gcdex(e1, e2)
u, v = int(u), int(v)
print(f"u = {u}, v = {v}")

# Xử lý trường hợp u hoặc v âm
if u < 0:
    c1_inv = pow(c1, -1, n)
    term1 = pow(c1_inv, -u, n)
else:
    term1 = pow(c1, u, n)

if v < 0:
    c2_inv = pow(c2, -1, n)
    term2 = pow(c2_inv, -v, n)
else:
    term2 = pow(c2, v, n)

recovered_m = (term1 * term2) % n
print(f'Message: {long_to_bytes(recovered_m).decode()}')