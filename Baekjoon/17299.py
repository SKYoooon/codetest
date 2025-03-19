import sys

list_size = int(sys.stdin.readline())
input_data = list(map(int, sys.stdin.readline().split()))

result = [-1 for _ in range(list_size)]
stack = []
count_dict = {}
for num in input_data:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
freq = [count_dict[num] for num in input_data]

for i in range(list_size):
    while stack and freq[stack[-1]] < freq[i]:
        result[stack.pop()] = input_data[i] 
    stack.append(i)  
print(' '.join(map(str, result)))