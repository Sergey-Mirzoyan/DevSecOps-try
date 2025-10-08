from random import randint
from math import *
import time
import timeit
import pickle
import numpy as np
import os
import sys
sys.set_int_max_str_digits(0)


# def fill(W,H):
    # current_field = next_field = [[0 for i in range(W)] for j in range(H)]
  ##  print("time.process_time_ns() = ", time.process_time_ns())
  ##  print("timeit.timeit() = ", timeit.timeit())
  ##  entrp = round((time.process_time_ns() * timeit.timeit()))#% (W*H)/2
  ##  entrp = float('0.' + str(entrp))
  ##  print("pre ENTROPY = ", entrp)
    # length = 0
    # long = len(str(min(W,H)))-1

    # nummy = lambda :int(str(timeit.timeit())[-long:]) % 3
    # nummy_1, nummy_2 = nummy(), nummy()

    # for j in range (W):
        # entrp_j = int(str(timeit.timeit())[-long:])
        # entrp_i = int(str(timeit.timeit())[-long:])
        # for i in range(H):
            # if i % entrp_i == 0 or j % entrp_j == 0:
                # current_field[i][j] = nummy_1

            # elif i > j and not (2 * i + j) % 4:
                # current_field[i][j] = 2 
            # else:
                # current_field[i][j-i] = 1
    # print_field(current_field, W,H, '_pre')
    # return current_field, next_field

def fill (W, H):
    current_field = next_field = [[0 for i in range(W)] for j in range(H)]
   # current_field = [[0 for i in range(W)] for j in range(H)]
    entrp = 0
    while entrp == 0:
        entrp = round((time.process_time_ns() * timeit.timeit()))#% (W*H)/2
        entrp = entrp % 10000
        # if entrp == 0:
            # print("entrp == 0")
    # entrp = 1877
    # print(entrp)
   # current_field = [[0 if i == entrp // W or j == entrp // H else 1 for i in range(W)] for j in range(H)]
    current_field = [[2 if i == W // entrp or j == H // entrp else 0 for i in range(W)] for j in range(H)]  
    for j in range (W):
     #   entrp_j = int(str(timeit.timeit())[-long:])
     #   entrp_i = int(str(timeit.timeit())[-long:])
        for i in range(H):
            if i != 0 and j!= 0:
                if entrp % i == 0 or entrp % j== 0:
                    current_field[i][j] = i % 3

                elif i > j and not (2 * i + j) % 4:
                    current_field[i][j] = 2 
                else:
                    current_field[i][j-(i%2)] = 1
    return next_field, current_field

def check_cell(current_field, x, y,W, H):
    count = 0
    
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j % H][i % W] != 0:
                count += 1
    # Zombie
    if current_field[y][x] == 2:
        count -= 1
        if count == 2 or count == 4:
            return 2
        return 0
    else:
        if count == 6:
            return 2

    # Alive
    if current_field[y][x] == 0:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

def life(W, H, next_field, current_field, tries):
    for k in range(tries):
        for x in range(1, W - 1):
            for y in range(1, H - 1):
                next_field[y][x] = check_cell(current_field, x, y,W,H)
          
        current_field = [*next_field]
    
    return current_field
        
def print_field(field, W, H, pref):
    # for i in range(len(field)):
        # for j in range(len(field[i])):
            # print(field[i][j], end='')
        # print()
    if H!= 0:    
        f = open('nums'+pref+'.txt','w')
        for i in range(len(field)):
            buf = ''
            for j in range(len(field[i])):
                buf += str(field[i][j])
            f.write(buf+'\n')
        f.close()
    else:
        f = open('nums'+pref+'.txt','w')
        buf = ''
        for i in range(W):
            buf += str(field[i])+'  '
        f.write(buf)
        f.close()
    
def convert_base(num, to_base, from_base):
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n,m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]

def Knut_test(U, flag):
    n = len(U)
    u2 = 0
    u_sum2 = 0
    # print(U)
    if isinstance(U[0], str):
        for i in range(len(U)):
            U[i] = int(U[i])

    u_sum2 = sum(U)**2
    U1U2 = 0
    for i in range(n-1):
        U1U2 += U[i]*U[i+1]
        u2 += U[i]**2
    C = (n*U1U2 - u_sum2)/(n*u2 - u_sum2)
    un = (-1)/(n-1)
    sigma = sqrt((n**2)/(((n-1)**2)*(n-2)))
    if flag == 1:
        if un - 2*sigma < C < un + 2*sigma:
            print('Хорошее значение - ', C)
            
        else:
            print('Нехорошее значение - ', C)
            
    return C

def choise_line(current_field):
    summ = 0
    summax = 0
    masmax = []
    cmin = 1
    x = []
    masK = []
    masnum = []
    KK = 0
    for k in range(1,len(current_field)-1):
        x = current_field[k]
        masK.append(k)
        # print(masK)
        num = ''
        num3 = ''
        for j in x:
            num += str(j)
            num3 += str(j)
        
        if sum(x) == 0:
            continue
        num = convert_base(num, 2, 3)
        num = list(num)
        
        c = Knut_test(num, 0)
        if c == '!!!':
            continue
        if abs(c) < cmin:
            masmax = num
            masnum = num3
            cmin = c
            KK = k
    # print("K: ", KK)
    return KK, masmax, masnum
    


# def read_bits(bits, length, count=None):
    # masnums = ''.join(str(i) for i in bits)
    # return masnums[:length]
    
# def ranging(bits, a, b):
    # bit_a = convert_base(a,3,10)
    # bit_b = convert_base(b,3,10)
    # len_a = len(bit_a)
    # len_b = len(bit_b)
    # flag = False
    # while flag == False:
        # len_fin = round((time.process_time_ns() * timeit.timeit()))#% (W*H)/2
        # len_fin = len_fin % max(len_a, len_b)
        # if len_fin == 0:
            # continue
        # else: 
            # flag = True  
    # len_num = max(len_a, len_b)
    # range_nums = read_bits(bits, len(bits))
    
    # return convert_base(range_nums, 10, 3)
   
# def ranging(bits, a, b):
    # bit_a = convert_base(a,3,10)
    # bit_b = convert_base(b,3,10)
    # len_a = len(bit_a)
    # len_b = len(bit_b)
    # if len_a > len_b: 
        # len_b,len_a = len_a, len_b
        # print(len_a)
    # flag = False
    # while flag == False:
        # len_fin = round((time.process_time_ns() * timeit.timeit()))#% (W*H)/2
        
        # len_fin = len_fin % (len_b+1)
        # if len_fin == 0:
            # continue
        # else:
        
        # range_nums = read_bits(bits, len(bits))
        # print("range_nums = ", range_nums)
        # num = float('0.'+convert_base(range_nums, 10,3))
        # print("converted range_nums = ", num)
        # normalized = (num-a)/(b-a)
        # if normalized > a and normalized < b:
            # flag = True
    
    # return convert_base(range_nums, 10, 3)
   
   
def normalized(nums, a, b):
    # minimum = min(nums)
    # maximum = max(nums)
    # norm_nums = []
    
    # for i in nums:
        # norm_nums.append((i - minimum) / (maximum - minimum) * b)
   
    # print(norm_nums)
    
    minimum = min(nums)
    maximum = max(nums)
    norm_nums = []
    f = int(sum(nums) / len(nums))
    # print(f)
    for i in nums:
        norm_nums.append((i - minimum) / (maximum - minimum) * b)
        # if i < f:
            # norm_nums *= -1
    # print(norm_nums)
    return norm_nums
    
rand_nums1 = []
rand_nums2 = []
from progress.bar import IncrementalBar

def read_bits(bits, count=None):
    masnums = ''.join(str(i) for i in bits)
    return masnums
    
def invers(bits):
    res = ''
    for i in bits:
        if i == '0':
            res += '1'
        elif i == '1':
            res += '2'
        else:
            res += '0'
    return res

def ranging1(W, H, current_field, tries, KK, a, b):
    # life(W, H, current_field, current_field, tries)
    rand_numsX = []
    rand_numsY = []
    X = []
    Y = []
    next_field = current_field 
    bar = IncrementalBar('Countdown', max = tries)
    for k in range(tries):
        for x in range(1, W - 1):
            for y in range(1, H - 1):
                next_field[y][x] = check_cell(current_field, x, y,W,H)
        # bar.next()
            if x < H:
                # print(x)
                bitsX = current_field[x]
                bitsY = np.array(current_field)[:,x]
                # print(bitsX)    
                # print(bitsY)
                range_numsX = read_bits(bitsX)
                range_numsY = read_bits(bitsY)
                # range_numsY = invers(range_numsY)
                numX = int(convert_base(range_numsX, 10,3))
                numY = int(convert_base(range_numsY, 10,3))
                # print(numX, " === ", numY)
                rand_numsX.append(numX)
                rand_numsY.append(numY)
                # print(rand_numsY)
        X = normalized(rand_numsX, a, b)
        
        Y = normalized(rand_numsY, a, b)
        current_field = [*next_field]
    # print(rand_numsX)
    
    return X, Y
    
def main(repeats, minimum, maximum):
    W, H = 250, 10
    tries = 10
    repeats = 100
    # minimum, maximum = 1000,100000
    
    # print("\tFill......................................................................./")
    current_field, next_field = fill(W,H)
    
    # print("\tlife......................................................................./")
    current_field = life(W, H, next_field, current_field, tries)
    
    # print("\tprint....................................................................../")
    print_field(current_field, W, H, '_current_field')
    
    # print("\tChose line................................................................./")
    # line_indx, line, line3 = choise_line(current_field)
    
    # print("\tR    anging..................................................................../")
    # current_field = ranging(current_field[line_indx], 1, 1000000, repeats)
    rand_numsX, rand_numsY = ranging1(W, H, current_field, repeats, 0, minimum, maximum)
    # print(len(rand_numsX))
    # print(rand_numsX)
    # print(len(rand_numsX))
    # print(len(rand_numsY))
    # print("\tprint_the_nums............................................................/")
    # print_field(rand_numsX, repeats, 0, '_X')
    # print_field(rand_numsY, repeats, 0, '_Y')
    # print(rand_numsX)
    return rand_numsX, rand_numsY
    
# start = time.time()    
# main(10, 0, 1)
# end = time.time()
# print('WORK TIME: ', end - start)