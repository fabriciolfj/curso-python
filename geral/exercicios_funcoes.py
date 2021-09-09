def func_2(val):
    return val


def func_1(func_2):
    return func_2


value = 1
print(str(func_1(func_2(value))))


#####################
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def funcao_oi(args):
    return f'{args}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


execucao = mestre(funcao_oi, 'fabricio')
execucao2 = mestre(saudacao, 'fabricio', saudacao='bom dia')
print(execucao)
print(execucao2)


#####################
def mestre(funcao, **kwargs):
    return funcao(**kwargs)


def funcao_oi(nome):
    return f'{nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


execucao = mestre(funcao_oi, nome='fabricio')
execucao2 = mestre(saudacao, nome='fabricio', saudacao='bom dia')
print(execucao)
print(execucao2)
