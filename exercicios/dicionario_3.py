clientes = {
    "cliente1": {
        'nome': 'Luiz',
        'sobreNome': 'Otavio'
    },
    'cliente2': {
        'nome': 'Fabricio',
        'sobreNome': 'Lucas'
    }
}

print(clientes.get('cliente1')['nome'])
print(clientes['cliente1'].keys())

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for k, v in clientes_v.items():
        print(f'\t{k}, {v}')

