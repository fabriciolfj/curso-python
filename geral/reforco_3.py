import math


def execute_saque(**kwargs):
    conta = kwargs.get('conta')
    op = kwargs.get('operacao')

    conta['saldo'] -= op['valor']
    conta['limite_saque'] -= 1

    if conta['limite_saque'] < 0:
        conta['saldo'] = conta['saldo'] - (op['valor'] * (1.89 / 100))

    return conta


def execute_op(**kwargs):
    conta = kwargs.get('conta')
    op = kwargs.get('operacao')

    if op['tipo'] == 'saque':
        return execute_saque(conta=conta, operacao=op)

    conta['saldo'] += op['valor']
    return conta


conta = {
    'saldo': 1000.00,
    'limite_saque': 2,
}

operacao = {
    'tipo': 'saque',
    'valor': 287.00
}

operacao1 = {
    'tipo': 'saque',
    'valor': 199.82
}

operacao2 = {
    'tipo': 'credito',
    'valor': 134.98
}

operacao3 = {
    'tipo': 'saque',
    'valor': 49.00
}

conta = execute_op(conta=conta, operacao=operacao)
conta = execute_op(conta=conta, operacao=operacao1)
conta = execute_op(conta=conta, operacao=operacao2)
conta = execute_op(conta=conta, operacao=operacao3)
conta['saldo'] = round(conta['saldo'], 2)
print(conta)
