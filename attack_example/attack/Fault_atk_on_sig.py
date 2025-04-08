from Crypto.Util.number import*
from functools import reduce
from math import gcd
import gmpy2

message = b'Notifications_give_to_staffs'
# Tạo khoá
p, q = getPrime(1024), getPrime(1024)
e = 65537
n = p*q

# Các thành phần được tạo từ server
print('-'*20, 'Secret component', '-'*20)
print(f'{p=}\n{q=}')


# Public
print('-'*20, 'Public component', '-'*20)
print(f'{message=}\n{n=}\n{e=}')

def chinese_remainder(rests, modulus):
    somme = 0
    prod = reduce(lambda a, b: a * b, modulus)
    for n_i, a_i in zip(modulus, rests):
        p = prod // n_i
        somme += a_i * gmpy2.invert(p, n_i) * p
    return int(somme % prod)

def sign(m, fault = False):
    dp = int(inverse(e,p-1))
    dq = int(inverse(e,q-1))
    sp = pow(m, dp, p)
    sq = pow(m, dq, q)
    if fault:
        sq += 1
    s = chinese_remainder([sp, sq], [p, q])
    return s

while True:
    m = int(input("Nhap m = "))
    s = sign(m, True)
    print(f'{s=}')

    # Attack
    print('-'*25, 'Attack', '-'*25)
    found_p = gcd(pow(s,e,n)-m, n)
    print(f'found_p = {found_p}')
    break
