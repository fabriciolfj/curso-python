def calc(value):
    try:
        return int(value) + 1
    except:
        return 0


x = 'Y'
result = 1
while x == 'Y':
    result = calc(result)
    print(f'Resultado: {result}')
    x = input('Deseja continuar ? ')

