def dividir_string(value):
    limit = 10
    return [value[i:i + 10] for i in range(0, len(value), 10)]


string = '01234567890123456789012345678901234567890123456789'
print(len(string))
print('.'.join(dividir_string(string)))
