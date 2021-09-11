def separar_list(value):
    return [value[i:i + 10] for i in range(0, len(value), 10)]


string = '012345678901234567890123456789012345678901234567890123456789'
lista_numeros = separar_list(string)

print(lista_numeros)
print('.'.join(lista_numeros))


test = [i for i in range(0, 100, 10)]
print(test)

#a partir do 0, percorre duas casas
print(string[0:2])

for i in range(0, len(string), 10):
    print(string[i:i + 10])