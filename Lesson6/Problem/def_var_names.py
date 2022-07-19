import ast

#Функция фарсинга имен переменных из кода
def var_names(prog_code):
    res = set()
    for anode in ast.walk(ast.parse(prog_code)):
        if type(anode).__name__ == 'Assign':
            res.update(t.id for t in anode.targets if type(t).__name__ == 'Name')
        elif type(anode).__name__ == 'For':
            if type(anode.target).__name__ == 'Name':
                res.add(anode.target.id)
    return res