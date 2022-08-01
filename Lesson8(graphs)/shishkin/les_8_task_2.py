"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""
from collections import deque


graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start, finish):
    length = len(graph)
    is_vizited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    _start = start

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_vizited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_vizited[i]:
        
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_vizited[i]:
                min_cost = cost[i]
                start = i

    message = get_message_way(parent, _start, finish)

    return cost, message


def get_message_way(parent, start, finish):
    way = deque([finish])
    i = finish
    if parent[i] == -1:
        raise Exception(f'Из вершины {start} нельзя попасть в вершину {finish}')

    while parent[i] != start and parent[i] != -1:
        way.appendleft(parent[i])
        i = parent[i]
    
    way.appendleft(start)
    return [_ for _ in way]


if __name__ == '__main__':
    try:
        s = int(input('От какой вершины идти: '))
        f = int(input('До какой вершины идти: '))
        cost, way = dijkstra(graph, s, f)
        print(cost)
        print('Список вершин, которые необходимо обойти: ', way)
    except Exception as err:
        print(err)

"""
От какой вершины идти: 2
До какой вершины идти: 5
[inf, 9, 0, 13, 3, 5, 4, inf]
Список вершин, которые необходимо обойти:  [2, 4, 6, 5]
"""
