# # # def binary_gap(num):
# # #     # Convert the number to binary
# # #     binary_str = bin(num)[2:]
# # #     # Initialize variables
# # #     current_gap = 0
# # #     max_gap = 0
# # #     # Iterate through each digit in the binary representation
# # #     for digit in binary_str:
# # #         if digit == '0':
# # #             # If it's a zero, increase the current gap
# # #             current_gap += 1
# # #         else:
# # #             # If it's a one, update the maximum gap if needed and reset the current gap
# # #             max_gap = max(max_gap, current_gap)
# # #             current_gap = 0
# # #     return max_gap

# # # print(binary_gap(num=9))
# # # KAA 001A
# # # KZZ 999Z
# # def count_possible_plate_numbers(start_plate, end_plate):
    
# #     start_ascii1 = ord(start_plate[0])
# #     end_ascii1 = ord(end_plate[0])

    
# #     possible_combinations = (end_ascii1 - start_ascii1 + 1) * 26 * 26
# #     print("possible_combinations", possible_combinations, end_ascii1 - start_ascii1)
# #     return possible_combinations


# # start_ascii1 = ord("K") 
# # end_ascii1 = ord("K")    

# # possible_combinations = (end_ascii1 - start_ascii1 + 1) *26* 26 *999* 26 
# # print("Total possible combinations:", possible_combination
# # def possible_combinations(start_plate, end_plate):
# #     start = ord(start_plate[0])
# #     end= ord(end_plate[0])
   

# # possible_combinations('KAA001A',"KZZ999Z")
# # possible_combinations_first_char = (end - start)
# def possible_combinations(start_plate, end_plate):
#     start = start_plate[1:]
#     end = end_plate[1:]
#     print(start, end)
#     # possible_combinations_first_char = (end - start+1)
#     return None


# result = possible_combinations('KAA001A', 'KZZ999Z')


# print("Possible combinations for the first character:", result)


# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].
def solution(N):
    # Step 1: Convert N to binary representation
    binary = bin(N)[2:]

    # Step 2: Find the positions of all the 1s in the binary representation
    ones = [i for i, x in enumerate(binary) if x == '1']

    # Step 3: Calculate the length of the longest binary gap
    max_length = 0
    for i in range(1, len(ones)):
        max_length = max(max_length, ones[i] - ones[i-1] - 1)

    return max_length
