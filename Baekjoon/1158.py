# Solution 1

import sys

input_data = sys.stdin.readline().split()
N = int(input_data[0])
K = int(input_data[1])

queue = [i for i in range(1, N+1)]
result = []
temp = 0

while queue:
    temp = temp + K -1
    if temp > len(queue):
        temp = temp % len(queue)
    
    result.append(queue.pop(temp))

print("<" + ", ".join(map(str, result)) + ">")


# Solution 2
import sys

input_data = sys.stdin.readline().split()
N = int(input_data[0])
K = int(input_data[1])

queue = [i for i in range(1, N+1)]
result = []
temp = 0

while queue:
    temp = (temp + K -1) % len(queue)
    
    result.append(queue.pop(temp))

print("<" + ", ".join(map(str, result)) + ">")
