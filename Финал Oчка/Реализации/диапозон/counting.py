'''
from collections import *
import matplotlib.pyplot as plt


f = open(input()+'.txt', "r")

def print_inventory(dct):
    print("Items held:")
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{} \t ({})".format(item, amount))
        
def counter(list_element):
    """Счетчик повторений элементов последовательности"""
    # создаем словарь, где будем хранить элемент списка в качестве, 
    # ключа, а количество его повторений будет значением
    count = {}
    # теперь считаем повторения элементов списка
    for element in list_element:
        if count.get(element, None):
            # если в словаре ключ со значением элемента списка
            # присутствует, то увеличиваем счетчик на 1
            count[element] += 1
        else:
            # если в словаре ключа со значением элемента 
            # спитска НЕТ, то создаем ключ со значением 1
            count[element] = 1

    # сортируем словарь по количеству повторений слов в тексте
    sorted_values = sorted(count.items(), key=lambda tpl: tpl[1], reverse=True)
    return dict(count) #dict(sorted_values), 


words = []
for i in f:
    words = i.split()

xword = [int(i) for i in words]
xword.sort()

# for i in xword:
    # print(i)
print(
        'min = ', min(xword),
        '\nmax = ', max(xword), '\n')
dictionary = counter(words)
plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
plt.show()
print_inventory(counter(words))
'''
from collections import *
import matplotlib.pyplot as plt


f = open(input()+'.txt', "r")

def print_inventory(dct):
    print("Items held:")
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{} \t ({})".format(item, amount))
        
def counter(list_element):
    """Счетчик повторений элементов последовательности"""
    # создаем словарь, где будем хранить элемент списка в качестве, 
    # ключа, а количество его повторений будет значением
    count = {}
    # теперь считаем повторения элементов списка
    for element in list_element:
        if count.get(element, None):
            # если в словаре ключ со значением элемента списка
            # присутствует, то увеличиваем счетчик на 1
            count[element] += 1
        else:
            # если в словаре ключа со значением элемента 
            # спитска НЕТ, то создаем ключ со значением 1
            count[element] = 1

    # сортируем словарь по количеству повторений слов в тексте
    sorted_values = sorted(count.items(), key=lambda tpl: tpl[1], reverse=True)
    return dict(sorted_values)


words = []
for i in f:
    words = i.split()

xword = [int(i) for i in words]
# xword.sort()
print(len(xword))
for i in range(len(xword)):
    if xword[i] == 1:
        print(xword[i], '\t', i)
print(
        'min = ', min(xword),
        '\nmax = ', max(xword), '\n')
dictionary = counter(words)
plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
plt.show()
print_inventory(counter(words))
# '''