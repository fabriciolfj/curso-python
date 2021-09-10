cadastro = {
    'Dados pessoal': {
        'nome': 'Fabricio',
        'sobrenome': 'Jacob',
        'documentos': {
            'cpf': '33967386855',
            'rg': '41723251x'
        }
    },
    'Endereco': {
        'tipo': 'Rua',
        'logradouro': 'Rua bahia',
        'numero': 25
    }
}

for cadastro, dados in cadastro.items():

    if cadastro == 'Dados pessoal':
        for documento, dado in dados['documentos'].items():
            print(f'{documento}-{dado}')

    if cadastro == 'Endereco':
        for key, value in dados.items():
            print(f'{key}-{value if type(value) == "int" else str(value)}')
