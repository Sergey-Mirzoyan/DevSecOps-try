from math import gcd

def bbs(bit_length, p, q, seed):
    n = p * q

    if gcd(p-1, q-1) != 2:
        raise ValueError("p-1 and q-1 are not relatively prime")

    x = seed
    result = ""

    for i in range(bit_length):
        x = x**2 % n
        result += str(x % 2)

    return result

p = 29996224275867
q = 32176447673467
seed = 10011
bit_length = 1000000

result = bbs(bit_length, p, q, seed)

with open("bbs.txt", "w") as f:
        f.write(result)