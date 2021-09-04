value = input("Digite seu nome: ")

if len(value) == 4:
    print("Nome curto")
elif 5 <= len(value) <= 6:
    print("Nome normal")
else:
    print("Nome grande")