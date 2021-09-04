nome = "Fabricio"
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)
print(nome, "tem", idade, "de idade e seu ims é", imc)
print(f'{nome} tem {idade} de idade e seu ims e {imc:.2f}')
print('{0} tem {1} de idade e seu imc e {2:.2f}'.format(nome, idade, imc))
