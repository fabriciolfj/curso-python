def convert_array_list_five_values(value):
    result = [v[0:5] for v in value.split('x')]
    return result


value = '12345x678x94562x3457x89456x13459x78979x87896x512314x8543x165'
result = convert_array_list_five_values(value)
print('.'.join(result))