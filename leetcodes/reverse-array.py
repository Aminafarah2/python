# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

# Write a function:

# def solution(A, K)
# #
# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

def solution(A, K):
    if not A or len(A) == 0 or K == 0:
        return A

    N = len(A)
    K %= N  # To handle the case where K > N

    # Reverse the entire array
    reverse(A, 0, N - 1)

    # Reverse the first K elements
    reverse(A, 0, K - 1)

    # Reverse the remaining elements (from K to N-1)
    reverse(A, K, N - 1)

    return A

def reverse(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1