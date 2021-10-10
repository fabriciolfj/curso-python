carrinho = []

carrinho.append(('Produto 1', 10))
carrinho.append(('Produto 2', 10))
carrinho.append(('Produto 3', 30))
carrinho.append(('Produto 4', 40))

soma = sum(float(v) for i, v in carrinho)
print(soma)
