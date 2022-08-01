# string = input('Введите строку для кодированния методом Хаффмана: ')
from binarytree import Node

string = "Как как"
chars = set(string)
chars_count = []
for el in chars:
    chars_count.append([el, string.count(el)])
chars_count = sorted(chars_count, key=lambda x: x[1])
print(chars_count)

while len(chars_count) != 2:
    el1 = chars_count.pop(0)
    el2 = chars_count.pop(0)
    print(el1, el2)
    count_new = el1[1] + el2[1]
    new_el = [[el1, el2], count_new]
    i = 0
    j = len(chars_count)
    while chars_count[i][1] < count_new:
        if i + 1 == len(chars_count):
            break
        i += 1
    if i+1 == len(chars_count):
        chars_count = chars_count + [new_el]
    else:
        chars_count = chars_count[:i] + [new_el] + chars_count[i:]
    print(chars_count)
el1 = chars_count.pop(0)
el2 = chars_count.pop(0)
count_new = el1[1] + el2[1]
chars_count = [[el1, el2], count_new]
print(chars_count)

if isinstance(chars_count[0], str):
    node = Node(None)
    node.left = Node(chars_count[0])
    node.right = Node(None)

while len(chars_count) != 1:
    for el in chars_count:
        if isinstance(el[0], str):
            pass

