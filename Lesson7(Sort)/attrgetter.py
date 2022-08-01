from collections import namedtuple
from operator import attrgetter

Person = namedtuple("Person", 'name, age')

p_1 = Person("Vasya", 45)
p_2 = Person("Anton", 24)
p_3 = Person("Olya", 20)

people = [p_1, p_2, p_3]
print(people)

result = sorted(people, key=attrgetter('age'))
print(result)
