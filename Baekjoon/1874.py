import sys

num_count = int(sys.stdin.readline())
target_list = [int(sys.stdin.readline()) for _ in range(num_count)]

stack = []
command_list = []
stack_num = 1

for num in target_list:
    while stack_num <= num:
        stack.append(stack_num)
        stack_num += 1
        command_list.append('+')
    if stack[-1] == num:
        stack.pop()
        command_list.append('-')
    else:
        print('NO')
        exit()

print('\n'.join(command_list))