# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

def graph_gen(n_vertex):
    return {i: set([j for j in range(n_vertex) if j != i]) for i in range(n_vertex)}


def dfs(graph, vertex=0, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)

    for el in graph[vertex] - visited:
        dfs(graph, el, visited)

    return visited


n_vertex = int(input('Введите количество вершин графа: '))
print(graph_gen(n_vertex))
print(dfs(graph_gen(n_vertex)))
