import sys
import time
"""
# checando se é um objeto iteravel
list1 = [1, 2, 3, 4]

print(hasattr(list, '__iter__'))  # iteravel true
print(hasattr(list, '__next__'))  # iterador false

######### convertendo para um iterador
list1 = iter(list1)
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))

# geradores, quando precisamos de valores que vao demorar muito tempo, muita memoria
lista = list(range(100000))
print(sys.getsizeof(lista))


#criando um gerador
def gerar_valores():
    for v in range(100):
        yield v
        time.sleep(0.1)


g = gerar_valores()
#eleé um iterável e um iterador
print(hasattr(g, '__next__'))
print(hasattr(g, '__iter__'))
for v in g:
    print(v)
"""
##outra forma de criar um gerador

lista = [x for x in range(10)] #cria uma lista
print(type(lista))
lista = {x for x in range(10)} #cria um conjunto
print(type(lista))
lista = (x for x in range(10)) #cria um gerador
print(type(lista))

list_new = [x for x in range(0,100)]

for value in list_new:
    print(value)