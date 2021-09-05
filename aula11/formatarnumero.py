"""
Formatando valores com modificadores

:s - Texto String
:d - Inteiros(int)
:f - Números com ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (Quantidade)(Tipo - s, d, ou f)

> - esquerda
< - direita
^- centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num_3 = 1150
print(f'{num_3:0>10}')
print(f'{num_3:0<10}')
print(f'{num_3:0^10}')
print(f'{num_3:0>10.2f}')


def calc_qtde(value):
    return int(50 - len(value) / 2)


nome = 'Fabricio Jacob'
print(f'{nome:#^{calc_qtde(nome)}}')

#nome_formatado = '{:@>14}'.format(nome)
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

nome_1 = 'Fabricio'
sobre_nome = 'Jacob'
nome_formatado2 = '{0:$>10} {1:$<7}'.format(nome_1, sobre_nome)
print(nome_formatado2)


nome_2 = nome.ljust(30, '#')
print(nome_2)
print(nome_2.lower())
print(nome_2.upper())
print(nome_2.title())
print(nome_2.replace('b', 'z'))