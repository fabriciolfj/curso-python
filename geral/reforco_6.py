import time


def create_generator():
    for i in range(1000):
        yield i
        print(i)
        time.sleep(0.1)


lista = [
    ('nome', 'Fabricio'),
    ('endereco', 'Rua teste')
]

result = {k: v for k, v in lista}
print(result)

print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__'))
g = create_generator()
for i in g:
    print(i)