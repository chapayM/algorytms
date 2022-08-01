
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 1. На улице встретились N друзей. Каждый пожал руку всем остальным
друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.'''

N = int(input('Количество друзей: '))
graph = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        graph[i][j] = 1
# Вывод матрицы смежности для ориентированного графа:
# for line in graph:
#     print(line)
handshakes_num = sum(map(sum, graph))
print(f'Всего рукопожатий: {handshakes_num}')
