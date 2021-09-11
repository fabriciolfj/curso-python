l1 = [1, 2, 3, 4, 5]
ex1 = [v * 2 for v in l1]

print(ex1)

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

l2 = ['Fabricio', 'Suzana']
ex4 = [v.replace('a', '@') for v in l2]
print(ex4)


tupla = (('chave', 'valor'), ('cahve2', 'valor2'))
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)
print(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0]
print(ex6)