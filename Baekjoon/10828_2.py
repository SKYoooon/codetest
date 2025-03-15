import sys

stack = []
num_of_input = int(sys.stdin.readline().strip())

for _ in range(num_of_input):
    input_data = sys.stdin.readline().strip().split()
    command = input_data[0]

    if command == 'push':
        stack.append(int(input_data[1]))
    elif command == 'top':
        output.append(str(stack[-1] if stack else -1))
    elif command == 'size':
        output.append(str(len(stack)))
    elif command == 'empty':
        output.append(str(0 if stack else 1))
    elif command == 'pop':
        output.append(str(stack.pop() if stack else -1))