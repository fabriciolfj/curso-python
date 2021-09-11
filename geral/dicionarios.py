cadastro = {
    "nome": "Fabricio",
    "idade": 36,
    "formacao": ['Cientista da computacao', 'Técnico em TI']
}


print(len(cadastro))
print(cadastro)
print(cadastro.get("idade"))
print(cadastro.keys())
print(cadastro.values())
print(cadastro.items())

cadastro['nome'] = 'Lucas'
cadastro['formacao'].append('Ensino medio')
print(cadastro.items())
