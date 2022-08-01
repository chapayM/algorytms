# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?

n_friends = int(input('Введите количество друзей: '))

# строим направленный граф, каждое руковожатие записывается зеркальными еденицами
friends_graph = [[1 if i != j else 0 for i in range(n_friends)] for j in range(n_friends)]
print(*friends_graph, sep='\n')

handshake = 0

for vertex in friends_graph:
    for el in vertex:
        handshake += el

# так-как рукопожатие имеет двунаправленную связь, то полученный результат уменьшаем в два раза
handshake = handshake / 2
print('Чтобы все друзья пожали друг другу руки потребуется %s рукопожатий' % int(handshake))



