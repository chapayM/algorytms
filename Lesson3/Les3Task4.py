# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint

def frequency(array):
    # result_dict = {}
    # for el in set(array):
    #     score = 1
    #     i = array.index(el)
    #     try:
    #         while array.index(el, i+1)>=0:
    #             score += 1
    #             i = array.index(el, i+1)
    #     except ValueError:
    #         result_dict[el] = score
    # return result_dic
    result = []
    set_array = list(set(array))
    for el in set_array:
        result.append(array.count(el))
    max_el = result[0]
    i = 0
    while i < len(result) - 1:
        if max_el < result[i + 1]:
            max_el = result[i + 1]
        i += 1
    index_max = result.index(max_el)
    return set_array[index_max]






list1 = [randint(0, 10) for _ in range(20)]
print(list1)
print(frequency(list1))
