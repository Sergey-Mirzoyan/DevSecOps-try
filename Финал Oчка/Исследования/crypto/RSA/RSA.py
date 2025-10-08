import random


def is_prime(n):
    """
    Определение, является ли число простым
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_large_prime():
    """
    Генерация большого простого числа
    """
    while True:
        p = random.randint(pow(10, 20), pow(10, 50))
        if is_prime(p):
            return p
        

def gcd(a, b):
    """
    Нахождение наибольшего общего делителя
    """
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    """
    Нахождение мультипликативно обратного числа
    """
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    phi_copy = phi
    while e > 0:
        temp1 = phi_copy // e
        temp2 = phi_copy - temp1 * e
        phi_copy = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if phi_copy == 1:
        return d + phi


def generate_keypair():
    """
    Генерация пары открытого и закрытого ключей
    """
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt(pk, message):
    """
    Шифрование сообщения
    """
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in message]
    return cipher


def decrypt(pk, message):
    """
    Расшифрование сообщения
    """
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in message]
    return ''.join(plain)
    
# Генерация пары ключей
public_key, private_key = generate_keypair()

# Шифрование сообщения
message = 'Hello, world!'
encrypted_message = encrypt(public_key, message)

# Расшифрование сообщения
decrypted_message = decrypt(private_key, encrypted_message)

# Проверка
assert message == decrypted_message