def saudacao(msg, nome):
    print(f'{msg} {nome}')


def soma(var1, var2, var3):
    sum = var1 + var2 + var3
    print(f'{str(sum)}')


def soma_percentual(value, percent):
    percent_format = int(str(percent).replace('%', '')) / 100
    value += value * percent_format
    return value


def example(value):
    if value % 2 == 0:
        return 'fizz'
    if value % 5 == 0 and value % 3:
        return 'FizzBuzz'
    if value % 5 == 0:
        return 'buzz'

    return value


print(soma_percentual(35, '41%'))
print(example(30))