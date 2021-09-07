texto = 'Fabricio Jacob'
index = 0

nova_string = ""
while index < len(texto):
    letra = texto[index]

    if letra == 'a':
        nova_string += 'A'
    else:
        nova_string += letra
    index += 1

print(nova_string)
