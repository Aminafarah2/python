def binary_gap(num):
   # Convert the number to binary
    binary_str = bin(num) [2:]
    # Initialize variables
    currnt_gap=0
    max_gap=0
    # Iterate through each digit in the binary representation
    for digit in binary_str:
        if digit == '0':
            # If it's a zero, increase the current gap
            current__gap += 1
        else:
             # If it's a one, update the maximum gap if needed and reset the current gap
            max_gap = max(max_gap, current_gap)
            current_gap = 0
    return max_gap    
print (binary_gap(num=9));