from collections import Counter

def diehard_birthdays(binary_string):
    # переводим строку из битов в список байтов
    byte_string = []
    for i in range(0, len(binary_string), 8):
        byte = int(binary_string[i:i+8], 2)
        byte_string.append(byte)

    # считаем количество каждого возможного значения байта
    byte_counts = Counter(byte_string)

    # вычисляем сумму квадратов количеств каждого байта
    sum_of_squares = sum(count ** 2 for count in byte_counts.values())

    # вычисляем общее количество байтов и средний квадрат
    num_bytes = len(byte_string)
    mean_square = num_bytes ** 2 / 256

    # вычисляем значение статистики
    stat_value = (sum_of_squares - mean_square) / mean_square

    # проверяем значение статистики
    if abs(stat_value - 1.0) < 0.001:
        return 'Passed'
    else:
        return 'Failed'    





filename = "../nums.txt"  # имя файла с битовой последовательностью
with open(filename, "r") as f:
    bits = f.read().strip()        

tests =    [
      diehard_birthdays,
      rank_test,
      decoder_test,
      OSPOTest,
      LempelZivTest,
      IRWTest,
      RWTest,
      LCGTest,
      PiZeroTest,
      PiOneTest,
      PiTwoTest,
      PiThreeTest,
      SigmaZeroTest,
      SigmaOneTest,
      sigma_two_test,
      sigma_three_test]
i = 1
for test in tests:
    result = test(bits)
    print(result)
