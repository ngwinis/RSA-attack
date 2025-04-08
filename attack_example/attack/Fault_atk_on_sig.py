from Crypto.Util.number import*
from functools import reduce
import gmpy2

# with open("flag.txt", "rb") as file:
#      flag = file.read()
flag = b'flag{this_is_real_flag}'
print(flag)
p, q = getPrime(1024), getPrime(1024)
e = 65537
n = p*q
d = inverse(e,(p-1)*(q-1))
c = pow(bytes_to_long(flag), e, n)

# print(f'{p=}\n{q=}')
print("n =",n)
print("e =",e)
print("c =",c)

def chinese_remainder(rests, modulus):
        somme = 0
        prod = reduce(lambda a, b: a * b, modulus)
        for n_i, a_i in zip(modulus, rests):
            p = prod // n_i
            somme += a_i * gmpy2.invert(p, n_i) * p
        return int(somme % prod)

def sign(m, fault = False):
    dp = inverse(e,p-1)
    dq = inverse(e,q-1)
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

    # Test
    from egcd import egcd
    found_p, _, _ = egcd(pow(s,e,n)-m, n)
    print(f'(found_p == p) = {found_p == p}')
    break

