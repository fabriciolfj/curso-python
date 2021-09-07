def is_contains(digitada, segredo):
    if digitada in segredo:
        return True

    return False


def gerar_palavra(digitadas, segredo):
    temp = ""
    for seg in segredo:
        if seg in digitadas:
            temp += seg
        else:
            temp += '_'

    return temp


segredo = 'perfume'
digitadas = []
tentativas = 3
while True:
    if tentativas == 0:
        print("Jogo finalizou")
        break

    letra_digitada = input('Digite a letra: ')

    if is_contains(letra_digitada, segredo):
        digitadas.append(letra_digitada)
    else:
        print("Letra nao esta no segredo, tente novamente")
        tentativas -= 1
        continue

    palavra = gerar_palavra(digitadas, segredo)

    if palavra == segredo:
        print("Acertou")
        break
    else:
        print(f"Ainda nao acertou: {palavra}")
