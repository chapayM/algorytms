# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой
# из модуля hashlib задача считается не решённой

import hashlib

def substr (s: str) -> int:

    if len(s) <= 1:
        return 0
    else:
        set_hash = {hashlib.sha1(s[0].encode('utf-8')).hexdigest()}
        for i in range(1, len(s)):
            for el in range(len(s) + 1 - i):
                h_subs = hashlib.sha1(s[el:el+i].encode('utf-8')).hexdigest()
                set_hash.add(h_subs)
        return len(set_hash)




s = input('Введите строку: ')
print(f'Введенная строка содержит {substr(s)} подстрок')
