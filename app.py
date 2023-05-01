# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

A = [1, 3, 6, 4, 1, 2]

A = [1, 2, 3]

# A = [ −1, −3]

def solution(A):
    # Implement your solution here
    n = len(A)
    if n == 0:
        return 1
    if n == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    A.sort()
    if A[0] > 1:
        return 1
        
    for i in range(1, n):
        if A[i] - A[i-1] > 1:
            return A[i-1] + 1
    return A[n-1] + 1




print(solution(A))


    # pass
