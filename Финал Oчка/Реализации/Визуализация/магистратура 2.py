from random import randint
from math import *
import time
#import pickle
import pygame
##from refactored import *
#import sys
#sys.path.insert(0, 'C/Users/serge/Desktop/CA final/sp800_22_tests/')
#import sp800_22_tests
import timeit
##print('no refactor')
##start = time.time()

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

def fill_1(W,H):
    current_field = next_field = [[0 for i in range(W)] for j in range(H)]
    #current_field = [[0 for i in range(W)] for j in range(H)]
    entrp = round((time.process_time_ns() * timeit.timeit()))#% (W*H)/2
    entrp = entrp % 10000
    entrp = 1877
    print(entrp)
    # current_field = [[0 if i == entrp // W or j == entrp // H else 1 for i in range(W)] for j in range(H)]
##    current_field = [[2 if i == W // entrp or j == H // entrp else 0 for i in range(W)] for j in range(H)]  
    for j in range (W):
        # entrp_j = int(str(timeit.timeit())[-long:])
        # entrp_i = int(str(timeit.timeit())[-long:])
        for i in range(H):
            if i != 0 and j!= 0:
                if entrp % i == 0 or entrp % j== 0:
                    current_field[i][j] = i % 3

                elif i > j and not (2 * i + j) % 4:
                    current_field[i][j] = 2 
                else:
                    current_field[i][j-i] = 1
    return next_field, current_field

def fill_2(W,H):
    current_field = next_field = [[0 for i in range(W)] for j in range(H)]
    current_field = [[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)] # 5,6,9,22,33
    return next_field, current_field
def fill_3(W,H):
    current_field = next_field = [[0 for i in range(W)] for j in range(H)]
    flag = 0
    for j in range(H):
        for i in range(W):
            if i % 2:
                current_field[j][i] = 1
            else:
                if flag!= 1 and j == 7:
                    current_field[j][i] = 2
                    flag = 1
                else:
                    current_field[j][i] = 0
    return next_field, current_field
    
def fill_4(W,H):
    current_field = next_field = [[0 for i in range(W)] for j in range(H)]

    for j in range(H):
        for i in range(W):
            if i % 2:
                current_field[j][i] = 2
            else:
                current_field[j][i] = 0
    return next_field, current_field

def fill_4(W,H):
    current_field = next_field = [[0 for i in range(W)] for j in range(H)]
    entrp = round(time.process_time_ns() * timeit.timeit()) // W
    print(entrp)
    for j in range(H):
        for i in range(W):
            if not i % entrp:
                current_field[j][i] = 1
            else:
                current_field[j][i] = 2
    return next_field, current_field
    
def filling(choice, W, H):
    if choice == 0:
        next_field, current_field = fill_1(W,H)
    if choice == 1:
        next_field, current_field = fill_2(W,H)
    if choice == 2:
        next_field, current_field = fill_3(W,H)    
    if choice == 3:
        next_field, current_field = fill_4(W,H)
        
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

def main(WIDTH,HEIGHT,TILE,FPS,P, choice):
    RES = WIDTH, HEIGHT
    W, H = WIDTH // TILE, HEIGHT // TILE
    
    next_field = []
    current_field = []
    next_field, current_field = filling(choice,W,H)
    pygame.init()
    surface = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()
    
    for k in range(P):
        surface.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
        [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
        # draw life            
    
        for x in range(W):
            for y in range(H):
                if current_field[y][x] == 1:
                    pygame.draw.rect(surface, pygame.Color('forestgreen'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
                if current_field[y][x] == 2:
                    pygame.draw.rect(surface, pygame.Color('red'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
                
                next_field[y][x] = check_cell(current_field, x, y,W, H)
            
        current_field = [*next_field]
        pygame.display.flip()
        clock.tick(FPS)

    summ = 0
    summax = 0
    masmax = []
    cmin = 1
    xmin = 0
    xmax = 1
    x = []
    line = 0
    ##################################################
    for k in range(1,len(current_field)-1):
        x = current_field[k]
        
        num = ''
        for j in x:
            num += str(j)
            
        if sum(x) == 0:
            continue
        num = convert_base(num, 2, 3)
        
        num = list(num)
    ##    print(len(num))
        c = Knut_test(num, 0)
        if abs(c) < cmin:
            line = k
            masmax = num
            cmin = c
    print("chosen line = ", line)
    ##for i in range(100):
    rand = [randint(xmin,xmax) for i in range(W)]
    
    ##    f = open('nums_rand.txt','w')
    ##    for i in range(len(rand)):
    ##        f.write(str(rand[i]))#+'\n')
    ##    f.close()
    ##tests(masmax, rand)

##    print(num)
    f = open('nums.txt','w')
    bits = 0
    for i in range(len(masmax)):
        # print(masmax[len(masmax)-i-1])
        f.write(str(masmax[i]))#+'\n')
    f.close()
    s = ''
    # for i in range(len(masmax)):
        
        # s += str(masmax[i])+' '
    # print(s)

    #pickle.dump(current_field, open("myfile.bin", "wb"))
    return s
    
    
#def main(WIDTH,HEIGHT,TILE,FPS,P, choice):
#    work(WIDTH,HEIGHT,15)
main(1500,800,6,0.5,15,0)

# main(1500,110,10,2,20,2)