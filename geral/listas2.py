l1 = [1, 2, 3]
#     0  1  2  3  4  5
l2 = [4, 5, 6, 7, 8, 9]

l1.append(9) #acrescenta um valor no final da lista

#del(l2[:2]) #quero excluir os 2 primeiros digitos da lista
del(l2[3:5]) #quero o 7 e 8, o ultimo nao é incluido (5)
print(l1)
print(l2)

print(max(l1))
print(min(l1))