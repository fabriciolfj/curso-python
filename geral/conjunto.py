# sets, so recebem valores, valores imutáveis, não respeitam ordem, não aceitam valores duplicados
# union |
# intersection &
# differente - mostra os dados do conjunto da esquerda, que não estão no conjunto da direita
# symmetric_difference ^ pega os elementos diferentes entre os conjuntos
"""
s1 = {1, 2, 3, 4, 5}
print(s1)

for v in s1:
    print(v)


s2 = set()
s2.add(1)
s2.add(2)
s2.add(0)
s2.update('abcdr') #ela itera a cada elemento, e adiciona cada um

s2.discard(0)

print(s2)

s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4, 5}
s3 = s1 | s2

print(s3)

s1 = {1, 2, 3, 4}
s2 = {8, 9, 3, 4, 5}
s3 = s1 & s2

print(s3)

s1 = {1, 2, 3, 4}
s2 = {8, 9, 3, 4, 5}
s3 = s1 - s2

print(s3)

s1 = {1, 2, 3, 4}
s2 = {8, 9, 3, 4, 5}
s3 = s1 - s2

print(s3)

"""

s1 = {1, 2, 3, 4}
s2 = {8, 9, 3, 4, 5}
s3 = s1 ^ s2

print(s3)
