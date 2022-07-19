import ast

prog = ("\ndef fact(i):\n    f=2\n    for j in range(2,i+1):\n        f = f*i\n"+
       "        i = i - 1\n    print ('The factorial of ',j,' is ',f)")
res = set()
for anode in ast.walk(ast.parse(prog)):
    if type(anode).__name__ == 'Assign':
        res.update(t.id for t in anode.targets if type(t).__name__ == 'Name')
    elif type(anode).__name__ == 'For':
        if type(anode.target).__name__ == 'Name':
            res.add(anode.target.id)
print('All assignments: ' + str(res))