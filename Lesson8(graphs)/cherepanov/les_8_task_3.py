
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 3. Написать программу, которая обходит не взвешенный ориентированный
граф без петель, в котором все вершины связаны, по алгоритму поиска в
глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на
вход число вершин.'''

from collections import deque


def make_graph(n):
    graph = []
    for i in range(n):
        graph.append([j for j in range(n) if j != i])
    return graph


def depth_first_search(graph, start, finish):
    length = len(graph)
    parent = [None] * length
    is_visited = [False] * length
    deq = deque([start])
    is_visited[start] = True
    while len(deq) > 0:
        current = deq.pop()
        if current == finish:
            break
        for vertex in graph[current]:
            if not is_visited[vertex]:
                is_visited[vertex] = True
                parent[vertex] = current
                deq.appendleft(vertex)
    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'
    cost = 0
    visited_vertexes = deque([finish])
    i = finish
    while parent[i] != start:
        cost += 1
        visited_vertexes.appendleft(parent[i])
        i = parent[i]
    cost += 1
    visited_vertexes.appendleft(start)
    return list(visited_vertexes)


n = int(input('Число вершин в графе: '))
start = int(input('Вершина начала: '))
finish = int(input('Вершина конца: '))
graph = make_graph(n)
way = depth_first_search(graph, start, finish)
if type(way) is list:
    print(f'Путь из вершины {start} в вершину {finish}: {way}')
else:
    print(way)
