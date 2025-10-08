import random
import struct
import prng2 as PRNG
import codecs
import textwrap

def bitstring_to_blocks(s):
    # Разбить последовательность на блоки в 8 символов
    blocks = textwrap.wrap(s, 8)
    print(len(blocks))
    return blocks

def bitstring_to_char(s):
    return chr(int(s, 2))

def generate_new_bit_string():
    # Эта функция должна генерировать новую битовую последовательность при необходимости
    # Я представлю ее просто в виде заглушки, возвращающей случайную последовательность битов длиной 24
    return PRNG.main(0)
    
def translate(bits):
    bit_array = bitstring_to_blocks(bits)
    for i in bit_array:
        print(bitstring_to_char(i), end='')
    return 0
# Пример использования функции
bit_string = '110011001010111001011000111101010111000110101'
filename = "../nums.txt"  # имя файла с битовой последовательностью
with open(filename, "r") as f:
    bit_string = f.read().strip()  
# bit_string = bit_string[:100]  
utf8_parts = translate(bit_string)#, 8)

print(utf8_parts)