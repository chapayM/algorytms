# from collections import Counter
#
# a = Counter()
# b = Counter('Антон Абрамов')
# c = Counter({'red': 2, 'blue': 4})
# d = Counter(cats=4, dogs=5)
#
# print(a, b, c, d, sep='\n')
#
# print(b['z'])
# b['z'] = 0
# print(b)
#
# print(list(b.elements()))
#
# print(b.most_common(2))
#
# g = Counter(a=4, b=3, c=-3, d=0)
# f = Counter(a=1, b=2, c=3, d=-2)
# g.subtract(f)
# print(g)
#
# print("-"*50)
# print(set(g))
# print(dict(g))
# g.clear()
# print(g)
#
# print("-"*50)
# x = Counter(a=3, b=1)
# y = Counter(a=1, b=2)
# print(x + y)
# print(x - y)
# print(x & y)
# print(x | y)
#
# print("-"*50)
# z = Counter(a=4, b=-5)
# print(+z)
# print(-z)

from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
c.clear()
print(b, c, sep='\n')

print('#'*50)
d = deque([i for i in range(5)], maxlen=7)
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)

print('#'*50)
f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(x, y, f)

print('#'*50)
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)
print(g)

g.reverse()
print(g)

g.rotate(3)
print(g)

print('#'*50)
with open('ip_log.txt', 'r', encoding='utf-8') as f:
    last_ten = deque(f, 10)

print(last_ten)
