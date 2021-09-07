segredo = "perfume"
tentativas = 3
while tentativas > 0:
    texto = input('Digite a senha: ')

    if texto == segredo:
        print("Acertou")
        break

    tentativas -= 1
else:
    print("Senha incorreta")


texto = list('Fabricio')
texto.pop()
print(texto)
print("fim")