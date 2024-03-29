#1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
#Примечания:
#a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
#b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

list_1 = [random.randint(-100, 99) for i in range(10)]
print(list_1)

def bubblesort(list):
    n = 1
    while n < len(list):
        swapped = False
        for i in range(len(list) - n):
            if list[i] > list[i + 1]:
                swapped = True
                list[i], list[i + 1] = list[i + 1], list[i]
        n += 1
        print(list)
        if swapped == False: # прерываем цикл, если перестановок больше не происходит
            return list
    return list

print(bubblesort(list_1))

