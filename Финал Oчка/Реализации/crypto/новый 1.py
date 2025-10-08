import random
import struct

# binary_string = ''
filename = "../nums.txt"  # имя файла с битовой последовательностью
with open(filename, "r") as f:
    bits = f.read().strip()   
    
# Определение размера ключа в битах
key_size = 256

# Разбиение последовательности битов на блоки размера ключа
key_blocks = [bits[i:i+key_size] for i in range(0, len(bits), key_size)]

# Преобразование каждого блока в число и преобразование его в последовательность байтов
key_bytes = b""
for block in key_blocks:
    block_int = int(block, 2)
    key_bytes += struct.pack('!Q', block_int)

# В итоге получаем ключ, состоящий из 128 случайных битов
key = key_bytes[:key_size//8]
print(key.hex())