dir = {
    'nome': 'fabricio',
    'endereco': 'Rua teste',
    (8, 4, 7): 'Tupla'
}

if 'nome' in dir:
    print(dir.get('nome'))

if dir.get('fone') is not None:
    print(dir.get('nome'))

dir['fone'] = '998888232'

if dir.get('fone') is not None:
    print(dir.get('fone'))

dir.update({'fone': '00000'})
print(dir.get('fone'))

del dir['fone']
print('fone' in dir)
print('fone' in dir.keys())
print('fabricio' in dir.values())

### quantidade de pares
print(len(dir))

##### iterando sobre um dicionario
for k in dir.values():
    print(k)

for k in dir.items():
    print(k[0], k[1])

for k, v in dir.items():
    print(f'{k} {v}')