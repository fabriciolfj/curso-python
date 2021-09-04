"""
and, or, not, in e not in
"""

nome = input("Digite seu nome:")

if nome.startswith('Fa') and nome.endswith("io"):
    print("Nome começa com Fa e termina com io")
elif 'z' not in nome:
    print(f"O caracter z não está no {nome}")
elif 'z' in nome:
    print(f"O caracter z está no {nome}")
else:
    print("Nenhuma condição atendida")