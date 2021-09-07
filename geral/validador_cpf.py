def calculo_primeiro_digito(values):
    acumulador = 0
    index = 0
    for n in range(10, 1, -1):
        if n < 2:
            break
        acumulador += int(values[index]) * n
        index += 1
    print(f"Total: {acumulador}")
    calc = 11 - (acumulador % 11)

    if calc > 9:
        return 0
    return calc


def calculo_segundo_digito(values, digito):
    acumulador = 0
    index = 0
    for n in range(11, 1, -1):
        if n < 3:
            break
        acumulador += int(values[index]) * n
        index += 1
    acumulador += 2 * digito
    print(f"Total: {acumulador}")
    calc = 11 - (acumulador % 11)

    if calc > 9:
        return 0
    return calc


cpf_informado = "35659662897"
cpf = list(cpf_informado)
primeiro_digito = calculo_primeiro_digito(cpf)
segundo_digito = calculo_segundo_digito(cpf, primeiro_digito)
novo_cpf = cpf_informado[:9] + str(primeiro_digito) + str(segundo_digito)
print(novo_cpf == cpf_informado)
