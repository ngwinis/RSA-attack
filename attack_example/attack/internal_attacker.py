from Crypto.Util.number import *
from sympy import mod_inverse

message = b'secret_message'
m = int.from_bytes(message, byteorder='big')

# Tạo khoá
p, q = getPrime(512), getPrime(512)
n = p * q
e_attacker = 65537
phi = (p - 1) * (q - 1)
d_attacker = int(mod_inverse(e_attacker, phi))
e_boss = 42667

# Các thành phần được tạo từ server
print('-'*20, 'Secret component', '-'*20)
print(f'{m=}\n{p=}\n{q=}')
print(f'{d_attacker=}')

# Public
ciphertext = pow(m, e_boss, n)
print('-'*20, 'Public component', '-'*20)
print(f'{n=}\n{e_attacker=}\n{e_boss=}\n{ciphertext=}')

# Attack
print('-'*25, 'Attack', '-'*25)
k = 1
phi_N = 0
while True:
    if (e_attacker * d_attacker - 1) % k == 0:
        phi_N = (e_attacker * d_attacker - 1) // k
        break
    k += 1

d_boss = mod_inverse(e_boss, phi_N)
decrypted_m = pow(ciphertext, d_boss, n)
decrypted_message = decrypted_m.to_bytes((decrypted_m.bit_length() + 7) // 8, byteorder='big')

print(f"phi_attacked = {phi_N}")
print(f"d_boss_attacked = {d_boss}")
print(f"msg_boss: {decrypted_message.decode()}")
