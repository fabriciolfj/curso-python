logged_user = False
msg = 'Usuario logado' if logged_user else 'Usuário não logado'
print(msg)

idade = input("Digite sua idade: ")

if not idade.isnumeric() :
    print("Digite um número")
else:
    print(f"Idade: {str(idade)}")
    print("Menor de idade" if int(idade) < 18 else "Maior de idade")