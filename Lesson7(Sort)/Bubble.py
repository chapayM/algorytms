# Сортировака пузырьком. Сложность O(n^2).
# Устойчивая. Тип - Обменная. Требует доп память - не требуется

import random

array = [i for i in range(10)]
random.shuffle(array)

print(array)

n = 1
count = 0
swap = True
while n < len(array) and swap == True:
    swap = False
    for i in range(len(array)-n):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            swap = True
        count += 1
    n += 1
    print(array)
print(count)

print(array)
