variavel = "Teste"


def func(**args):
    global variavel
    variavel = args.get('describe')


func(describe="fabricio")
print(variavel)
