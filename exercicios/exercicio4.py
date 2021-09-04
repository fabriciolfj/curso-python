value = input("Digite um número inteiro: ")

#valida somente números positivos5
if not value.isdigit():
    print("Você digitou um valor não inteiro")
    exit()

rest = int(value) % 2

if rest == 0:
    print("Número par")
else:
    print("Número impar")
