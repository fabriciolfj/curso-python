#unindo iteraveis
#zip uni até a menor lista
#zip_longest uni até a maior lista

from itertools import zip_longest, count

estados = ['SP', 'MG', 'BA']
cidades = ['São Paulo', 'Belo horizonte', 'Salvador', 'Monte Belo']

indice = count()
"""
#nao use count com o zip_longest
estados_cidades = zip_longest(estados, cidades, fillvalue="Estado")
for v in estados_cidades:
    print(v)
"""

#zip
estados_cidades = zip(indice, estados, cidades)

for i, e, c in estados_cidades:
    print(f'{i} - {e} - {c}')



