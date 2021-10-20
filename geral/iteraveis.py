#iteraveis, vou consumindo os dados, caso eu queria eles dp, somente mostrará os que não foram consumidos
nome = 'Fabricio Jacob'
iteravel = iter(nome)

print(next(iteravel))
print(next(iteravel))
print(next(iteravel))
print(next(iteravel))

print('#' * 100)
#vai imprimir o restante do nome que nao foi dado next
for n in iteravel:
    print(n)

print('#' * 100)
#geradores tem o mesmo comportamento
geradores = (letra for letra in nome)

print(next(geradores))
print(next(geradores))
print(next(geradores))

print('#' * 100)

for v in geradores:
    print(v)

print('#' * 100)
#a forma abaixo não sobre desse problema
for v in nome:
    print(v)

print('#' * 100)
print("normal")

for v in nome:
    print(v)