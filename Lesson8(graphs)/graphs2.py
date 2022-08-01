from collections import namedtuple

graph = []

graph.append([1, 2])
graph.append([0, 2, 3])
graph.append([0, 1])
graph.append([1])
# проблема долгого происка
print(*graph, sep='\n')

# ускорение работы графа

print('*'*80)

graph_2 = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1]
}

print(graph_2)

#Проверка что из вершины 3 можно попасть в вершину 1
if 3 in graph_2[1]:
    print(True)

#Граф с весом
print('*'*80)

Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph_3 = []

graph_3.append([Vertex(1, 2), Vertex(2, 3)])
graph_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph_3.append([Vertex(0, 3), Vertex(1, 2)])
graph_3.append([Vertex(1, 1)])

print(*graph_3, sep='\n')

#Проверка что из вершины 3 можно попасть в вершину 1
for v in graph_3[1]:
    if v.vertex == 3:
        print(True)

#Графы удобно хранить в специально созданном объекте
class Graph:
    def __init__(self, vertex, edge, spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam
