#반복문 Memoization
#O(n)

n = int(input())

arr = [-1] * (n+2)

# Initial Value Setting
arr[0] = 0
arr[1] = 1

for i in range(2,n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])