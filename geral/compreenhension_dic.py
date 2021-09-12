lista = [
    ('chave_1', 2),
    ('chave_2', 4),
    ('chave_3', 5),
]

d1 = {x: y**2 for x, y in lista}
print(d1)


d2 = {x for x in range(8)} #gera um conjunto
print(d2)