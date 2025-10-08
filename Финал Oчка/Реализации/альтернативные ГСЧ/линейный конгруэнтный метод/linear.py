import time
start = time.time()
def lcg(x, a, c, m):
    while True:
        x = (a * x + c) % m
        yield x


def random_uniform_sample(n, interval, seed=0):
    a, c, m = 1103515245, 12347, 2 ** 31
    bsdrand = lcg(seed, a, c, m)

    lower, upper = interval[0], interval[1]
    sample = []

    for i in range(n):
        observation = (upper - lower) * (next(bsdrand) / (2 ** 31 - 1)) + lower
        sample.append(round(observation))

    return sample

# 30 numbers between 0 and 100
rus = random_uniform_sample(1200000, [0, 1])
##print(rus)
f = open('nums.txt','w')
for i in range(len(rus)):
    f.write(str(rus[i]))#+'\n')
f.close()
end = time.time()
print("WORK TIME: ", end - start)