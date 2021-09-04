value = input("Digite um número inteiro: ")
try:
    result = int(value)
except:
    print("Voce não digitou um valor inteiro")
    exit()

rest = result % int(2)

if rest == 0:
    print("Número par")
else:
    print("Número impar")
