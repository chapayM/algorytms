# year = int(input())
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')
import random

my_typle = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
print((my_typle))
for column in my_typle:
    for item in column:
        print(f'{item:>4}', end='')
    print()

# def gcb(a, b):
#     if b == 0:
#         return a
#     return gcb(b, a%b)
#
# print(gcb(12, 6))
# a=b=0
# n = 1
# while n>0:
#     if n%2==0:
#         a+=1
#     else:
#         b+=1
#     n = n//10
# print(a, b)




