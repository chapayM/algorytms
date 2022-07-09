# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

def pos_even_number(array):
    return [pos for pos, el in enumerate(array) if el % 2 == 0]


print(pos_even_number([8, 3, 15, 6, 4, 2]))
