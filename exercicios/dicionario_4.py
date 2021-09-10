import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['fabricio', 'lucas']}
v = copy.deepcopy(d1)

v[1] = 'z'
v['d'][0] = 'Jorge'

print(d1)
print(v)

### convertendo para dicionario
list = [
    ['C1', 1],
    ['C2', 2]
]

d1 = dict(list)
print(list)
print(d1)

### eliminar uma chave
d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d2 = {
    5: 6,
    7: 9
}

##pagando a chave 1
d1.pop(1)
print(d1)

### concatenando
d1.update(d2)
print(d1)