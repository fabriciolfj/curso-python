value = int(input("Qual o horário atual: "))


if value <= 11:
    print("Bom dia")
elif 12 <= value <= 17:
    print("Boa tarde")
elif 18 <= value <= 24:
    print("Boa noite")
else:
    print("Horario inválido")
