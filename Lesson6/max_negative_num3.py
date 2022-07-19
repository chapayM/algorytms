# Вариант 3 - через перебор возможных ответов, посредством движения от -1 в сторону уменьшения
def max_negative_number3(array):
    i = -1
    while True:
        for el in array:
            if el == i:
                return f'Максимальное отрицательное чиcло {el} расположено на {array.index(el)} месте в массиве.', \
                       locals()
        i -= 1