import sys

def Binary_Search(A, X):
    start = 0
    end = len(A)-1
    
    while start <= end:
        mid = (start + end) // 2
        if X == A[mid]:
            return 1
        elif X > A[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(input())
X = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    print(Binary_Search(A, X[i]))