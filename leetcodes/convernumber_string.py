def number_to_string(num):
    str_num = str(num)
    return str_num

print(number_to_string(9))
def number_to_string(*args):
    result = []
    for num in args:
        str_num = str(num)
        result.append(str_num)
    return result

print(number_to_string(9, 10, 23))

