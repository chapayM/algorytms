
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он
дополнительно возвращал список вершин, которые необходимо обойти.'''

graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    cost[start] = 0
    min_cost = 0
    visited_vertexes_list = [[] for _ in range(length)]
    visited_vertexes_list[start] = [start]
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start                
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    for i, vertex in enumerate(parent):
        if vertex > -1:
            visited_vertexes_list[i] = [i, vertex]
            while vertex > -1:
                vertex = parent[vertex]
                if vertex > -1:
                    visited_vertexes_list[i].append(vertex)
            visited_vertexes_list[i] = visited_vertexes_list[i][::-1]
    return cost, visited_vertexes_list


s = int(input('Вершина для старта: '))
cost, visited_vertexes = dijkstra(graph, s)
for i, line in enumerate(visited_vertexes):
    print(f'Кратчайший путь от вершины {s} до {i}: {line}; длина: {cost[i]}')