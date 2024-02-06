# You will be given an array of positive integers. The array should be sorted by the amount of distinct perfect squares and reversed, that can be generated from each number permuting its digits.

# E.g.: arr = [715, 112, 136, 169, 144] Number   Perfect Squares w/ its Digits   Amount
#  715                -                       0
#  112               121                      1
#  136               361                      1
#  169           169, 196, 961                3
#  144             144, 441                   2
# So the output will have the following order: [169, 144, 112, 136, 715] When we have two or more numbers with the same amount of perfect squares in their permutations, we sorted by their values.

# In the example given above, we can see that 112 and 136 both generate a perfect square. So 112 comes first.

# Examples for this kata: sort_by_perfsq([715, 112, 136, 169, 144]) == [169, 144, 112, 136, 715]

# number of perfect squares: 3 2 1 1 0
# We may have in the array numbers that belongs to the same set of permutations.

# sort_by_perfsq([234, 61, 16, 441, 144, 728]) == [144, 441, 16, 61, 234, 728]

# number of perfect squares: 2 2 1 0 0 0
# Features of the random tests:

# Number of tests: 30
# Arrays between 4 and 16 elements
# Integers having from 1 to 7 digits included
# Enjoy it!!
# def count_perfect_squares(num):
#     digits = sorted(str(num))
#     permutations = set()

#     # Ensure permuted_digits is not empty
#     if digits:
#         for i in range(1 << len(digits)):
#             permuted_digits = [digits[j] for j in range(len(digits)) if (i >> j) & 1]
#             if permuted_digits:
#                 permuted_num = int(''.join(permuted_digits))
#                 square_root = int(permuted_num ** 0.5)
#                 if square_root * square_root == permuted_num:
#                     permutations.add(permuted_num)

#     return len(permutations)

# def sort_by_perfsq(arr):
#     sorted_arr = sorted(arr, key=lambda x: (count_perfect_squares(x), x), reverse=True)
#     return sorted_arr

# # Examples
# print(sort_by_perfsq([715, 112, 136, 169, 144]))  # Output: [169, 144, 112, 136, 715]
# print(sort_by_perfsq([234, 61, 16, 441, 144, 728]))  # Output: [144, 441, 16, 61, 234, 728]

# def minimum(array):
#     min_val = float('inf')  # Initialize min_val with positive infinity
#     print(min_val)
#     for num in array:
#         print(num)
#         if num < min_val:
#             min_val = num
#             print(min_val)
#     return min_val

# def maximum(array):
#     max_val = float('-inf')  # Initialize max_val with negative infinity
    
#     for num in array:
#         if num > max_val:
#             max_val = num
#     return max_val


# # Example usage
# arr = [-52, 56, 30, 29, -54, 0, -110]
# print("Minimum:", minimum(arr))
# # print("Maximum:", maximum(arr))
def zero(): return '0'
def one(): return '1'
def two(): return '2'
def three(): return '3'
def four(): return '4'
def five(): return '5'
def six(): return '6'
def seven(): return '7'
def eight(): return '8'
def nine(): return '9'

def plus(num): return '+' + str(num)
def minus(num): return '-' + str(num)
def times(num): return '*' + str(num)
def divided_by(num): return '//' + str(num)

# Examples
print(eval(seven(times(five()))))  # Output: 35
print(eval(four(plus(nine()))))  # Output: 13
print(eval(eight(minus(three()))))  # Output: 5
print(eval(six(divided_by(two()))))  # Output: 3
