list = ['Banana', 'Maçã']
for value in list:
    if value.lower().startswith('j'):
        continue
    print(value)
else:
    print("não existe palavra que inicia com j")
