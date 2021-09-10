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

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for k, v in clientes_v.items():
        print(f'\t{k}, {v}')

