#vem como uma tupla, tupla é imutavel
#**kwargs para argumentos nomeados
def fun(*args, **kwargs):
    #args = list(args) caso queira converter para uma lista
    # print(args[0])
    # print(args[-1])
    print(args)
    print(kwargs.get('nome'))
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)


lista = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]
# n1, n2, *n = lista
# print(n1, n2, n)

fun(1, 2, 3, 4, 5)
fun(*lista, *lista2, nome='Fabricio', sobrenome='Jacob', idade='36') #para nao desempacotar, no caso irá mesclar as duas listas em uma tupla
