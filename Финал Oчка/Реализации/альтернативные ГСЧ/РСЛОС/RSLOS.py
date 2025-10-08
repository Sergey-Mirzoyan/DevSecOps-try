# определение функции для регистра сдвига
def shift_register(lfsr, taps):
    output = lfsr[-1] ^ lfsr[taps[0]] ^ lfsr[taps[1]] ^ lfsr[taps[2]]
    return [output] + lfsr[:-1]

# установка начального значения регистра
lfsr = [1, 0, 1, 1, 0, 0, 1, 1]

# установка точек обратной связи для регистра
taps = [0, 2, 3, 5]

# определение количества выходных бит
num_bits = 1000000

# генерация последовательности бит с помощью регистра сдвига
output_bits = []
for i in range(num_bits):
    output_bits.append(str(lfsr[-1]))
    lfsr = shift_register(lfsr, taps)

# сохранение результата в файл
with open("nums.txt", "w") as f:
    f.write("".join(output_bits))
