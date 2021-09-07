nome = input("Digite seu nome: ")

print(nome or "Você não digitou nada.")


a = 0 # returna false
b = None # returna false
c = False # returna false
d = [] # returna false
e = {} # returna false
f = 22 # returna true
g = 'Luiz' # returna true

variavel = a or b or c or d or e or f or g
print(variavel) # vai printar o primeiro que deu true, no caso 22