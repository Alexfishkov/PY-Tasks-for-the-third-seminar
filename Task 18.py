# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import os
import random
os.system('CLS')

list = []
n = int(input("Введите число элементов в массиве (1-50) => "))
number = int(input("Введите ваше натуральное число (0-30) => "))

list.append(random.randint(0,20))
difference = abs(number-list[0])
ndif = 0

for i in range (1,n):
    list.append(random.randint(0,20))
    if (abs(number-list[i]) < difference):
        difference = abs(number-list[i])
        ndif = i

print("Был задан случайным образом такой массив:")
print(list)
print(f"Самым ближайшим в нём элементом к вашему числу является: {list[ndif]}")
