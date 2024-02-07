# def number_to_string(num):
#     str_num = str(num)
#     return str_num

# print(number_to_string(9))
# def number_to_string(*args):
#     result = []
#     for num in args:
#         str_num = str(num)
#         result.append(str_num)
#     return result

# print(number_to_string(9, 10, 23))

import random

def generate_number_plate():
    letters = [chr(i) for i in range(65, 91)]  # A to Z in ASCII
    digits = [str(i) for i in range(10)]  # 0 to 9
    plate = ''.join([random.choice(letters) for _ in range(2)]) + ''.join([random.choice(digits) for _ in range(2)]) + ' ' + ''.join([random.choice(letters) for _ in range(3)])
    return plate

# Example usage

print(generate_number_plate())  # Output: "AB12 XYZ"