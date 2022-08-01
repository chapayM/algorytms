"""
Задание 1
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). 
Выведите на экран исходный и отсортированный массивы.

Примечания:
a. алгоритм сортировки должен быть в виде функции, 
    которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться 
    сортировка пузырьком. Улучшенные версии сортировки, 
    например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random


def get_array(size: int, left_border: int = None, right_border: int = None) -> list:
    """Получить shuffle массив случайных чисел от левой границы до правой,
        либо от 0 до size при дефолтных значениях границ"""
    if left_border is not None and right_border is not None:
        if left_border > right_border:
            left_border, right_border = right_border, left_border
        array = [random.randint(left_border, right_border) for _ in range(size)]
    else:
        array = [_ for _ in range(size)]
    random.shuffle(array)
    return array


def bubble_sort(array):
    """Алгоритм пузырьковой сортировки"""
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


if __name__ == '__main__':
    array = get_array(10, -100, 99)
    print(array)
    bubble_sort(array)
    print(array)
