# Сортировака ШЕлла. Сложность O(n^2) максимальная, до O(n (log n)^2 или O(n^3/2).
# Неустойчивая. Тип - Вставками. Требует доп память - не требуется


import random

array = [i for i in range(10)]
random.shuffle(array)

print(array)

# Сортировка Шелла
def shell_sort(array):

    assert len(array) < 4000, 'Массив слишком большой. Используйте другую соритровку!'

    def new_increment(array):

        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750] # Имперически полученные оптимальыне значения
                                                      # инкремента(шага) для сотрировки

        while len(array) <= inc[-1]: # Обрезание списка инкремента для работы с заданным массивом
            inc.pop()

        while len(inc) > 0: # через yield запоминаем последнее состояние функции
            yield inc.pop()

    count = 0

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                count += 1
    print(count)

shell_sort(array)
print(array)