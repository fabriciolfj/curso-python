string = "O Brasil é o pais do futebol, o Brasil e penta."
list_1 = string.split(' ')
list_2 = string.split(',')

for valor in list_1:
    print(f"A palavra {valor} apareceu {list_1.count(valor)}x na frase.")

for valor in list_2:
    print(valor.strip().title()) #remove o espaco no inicio e fim do string