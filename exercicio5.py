import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


value = input("Digite um número inteiro: ")

if not is_number(value):
    print("Digitou um valor inválido")
    exit()

rest = int(value) % 2

if rest == 0:
    print("Número par")
else:
    print("Número impar")
