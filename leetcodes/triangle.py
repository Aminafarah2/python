def solution(A):
    A = sorted([element for element in A if element > 0])
    for i in range(0, len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 
    return 0
# Example usage
input_list = [10, 2, 5, 1, 8, 20]
print(solution(input_list))