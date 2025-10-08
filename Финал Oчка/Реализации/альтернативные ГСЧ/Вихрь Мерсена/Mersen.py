import math

def generate_binary(x):
    if x <= 0.5:
        return 0
    else:
        return 1
        
# Функция для генерации вихря Мерсена
def mersenne_number(n):
    return 2**n - 1

# Создание генератора случайных чисел
def mersenne_twister(seed):
    # Инициализация констант
    n = 624
    m = 397
    a = 0x9908B0DF
    upper_mask = 0x80000000
    lower_mask = 0x7FFFFFFF

    # Инициализация массива MT
    mt = [0] * n
    mt[0] = seed
    for i in range(1, n):
        mt[i] = (1812433253 * (mt[i-1] ^ (mt[i-1] >> 30)) + i) & 0xFFFFFFFF
    
    # Генерация случайных чисел
    while True:
        for i in range(n):
            x = (mt[i] & upper_mask) + (mt[(i+1) % n] & lower_mask)
            xA = x >> 1
            if x % 2 != 0:
                xA ^= a
            mt[i] = mt[(i + m) % n] ^ xA
        y = mt[0]
        y ^= (y >> 11)
        y ^= ((y << 7) & 0x9D2C5680)
        y ^= ((y << 15) & 0xEFC60000)
        y ^= (y >> 18)
        yield generate_binary(y / (mersenne_number(32) - 1)) # Возвращаем случайное число в диапазоне от 0 до 1

# Создать генератор случайных чисел с начальным значением 5489
mt = mersenne_twister(5489)
buf = ''
# Генерировать 10 случайных чисел
f = open('nums.txt','a')
for i in range(1200000):
    f.write(str(next(mt)))
f.close()