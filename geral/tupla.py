#diferença entre tupla e lista, que tupla e imutavel nao consigo adicionar elementos
minhatupla = (1, 2, 3)
print(minhatupla)
print(minhatupla[0])

####### concatenando
t1 = 1, 2, 3, 4, 'fabricio'
t2 = 5, 6, 7
t3 = t1 + t2

n1, n2, *_, nultimo = t3

print(nultimo)