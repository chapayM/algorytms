"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s: str) -> dict:
    """Возвращает словарь символьных кодов Хаффмана, по переданной строке"""
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _, left = heapq.heappop(h)
        freq2, _, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    
    code = {}
    if h:
        [(_, _, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(s: str, codes: dict) -> str:
    """Декодирование закодированной строки Хаффмана"""
    result = ''
    _s = s
    dataset = sorted(codes.items(), key=lambda t: len(t[1]))
    while _s:
        for simbol, code in dataset:
            lenght = len(code)
            if lenght > len(_s):
                continue
            if _s[:lenght] == code:
                _s = _s[lenght:]
                result += simbol
                break
    return result


if __name__ == "__main__":
    s = input('Введите строку для кодирования по алгоритму Хаффмана: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))

    print('\n', 'Закодированная строка: ', encoded, '\n')
    source = huffman_decode(encoded, code)
    print('\n', 'Раскодированная строка: ', source, '\n')

    
"""
Введите строку для кодирования по алгоритму Хаффмана: Привет медвед!
 : 1110
!: 010
П: 1010
в: 011
д: 100
е: 00
и: 1100
м: 1111
р: 1011
т: 1101

 Закодированная строка:  101010111100011001101111011110010001100100010 


 Раскодированная строка:  Привет медвед!
"""
