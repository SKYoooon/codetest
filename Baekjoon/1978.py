import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
count = 0
for num in nums:
    if num == 1:
        continue
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        count += 1
print(count)