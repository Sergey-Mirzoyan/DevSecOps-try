import random
import prng as PRNG
# import prng1 as PRNG
# import prng2 as PRNG
from matplotlib import pyplot as plt
def count_pi(n,X, Y):
    i = 0
    count = 0
    # print(X)
    # n - общее количество набранных баллов
    for i in range(len(X)):
                 # Произвольно генерировать координаты x, y
        # x = random.random()
        # y = random.random()
                 # Если x квадрат + y квадрат <1, это означает, что он находится внутри круга
        # print(Y)
        if (pow(X[i], 2) + pow(Y[i], 2)) < 1:
            count += 1
            # print(i)
        i += 1
         # Значение π: 4 * (точки, попадающие в круг / общее количество баллов)
    # print(count)
    return 4 * (count / n)
 
n = int(input("N = "))
# minimum = int(input("minimum = "))
# minimum = int(input("minimum = "))
minimum = 0
maximum = 0.999

X = []
Y = []
for i in range(n):
    cordsX,cordsY = PRNG.main(n, minimum, maximum)    
    pi = count_pi(n, cordsX, cordsY)
    print("Value of Pi: ", pi)
    X.append(cordsX)
    Y.append(cordsY)
plt.scatter(X, Y)
plt.show()