import sys
list_size = int(sys.stdin.readline())
input_data = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(list_size)]
stack = []

for i in range(list_size):
    while stack and input_data[stack[-1]] < input_data[i]:
        result[stack.pop()] = input_data[i]
    stack.append(i)
print(' '.join(map(str, result)))


# import sys # 시간 초과

# list_size = int(sys.stdin.readline())
# input_data = list(map(int, sys.stdin.readline().split()))
# result = []

# for i in range(list_size-1):
#     comparison_num = input_data[i]
#     for j in range(i+1, list_size):
#         if comparison_num < input_data[j]:
#             result.append(input_data[j])
#             break
#         elif j == list_size-1:
#             result.append(-1)
#             break

# result.append(-1)

# print(' '.join(map(str, result)))