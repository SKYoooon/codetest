import sys
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    for i in range(min(A,B),0, -1):
        if A%i == 0 and B%i == 0:
            print(A*B//i)
            break