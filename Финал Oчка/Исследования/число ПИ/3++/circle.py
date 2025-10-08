import random
from progress.bar import IncrementalBar

# import prng as PRNG
# import prng1 as PRNG
import prng2 as PRNG
from matplotlib import pyplot as plt
def count_pi(n,X, Y):
    i = 0
    count = 0
    # print(X)
    # n - общее количество набранных баллов
    n = len(X)
    for i in range(n):
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
    print()
    print(count)
    # print(4 * (count / n))
    return 4 * (count / n)
 
n = int(input("N = "))
# minimum = int(input("minimum = "))
# minimum = int(input("minimum = "))
minimum = 0
maximum = 0.999

X = []
Y = []
bar = IncrementalBar('Countdown', max = n)
    
for i in range(n):
    cordsX = PRNG.main(minimum, maximum)
    cordsY = PRNG.main(minimum, maximum)
    bar.next()
    pi = count_pi(n, cordsX, cordsY)
    # print("Value of Pi: {:.5f}".format(pi))
    # print("Value of Pi: ", pi)
    X.append(cordsX)
    Y.append(cordsY)

resX = []
resY = []
for x in X:
    resX.extend(x if isinstance(x, list) else [x])
for y in Y:
    resY.extend(y if isinstance(y, list) else [y])
print(len(resX))
pi = count_pi(n, resX, resY)
print("FINAL Pi: ", pi)

figure, axes = plt.subplots()
Drawing_colored_circle = plt.Circle(( 0 , 0 ), 1, fill=False )
axes.scatter(resX, resY)
axes.set_aspect( 1 )
axes.add_artist( Drawing_colored_circle )
plt.title( 'Colored Circle' )
plt.show()