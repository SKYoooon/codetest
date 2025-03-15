import sys
stack = []
num_of_input = int(sys.stdin.readline())

for _ in range(num_of_input):
    input_data = sys.stdin.readline().split()

    if input_data[0] =='push':
        stack.append(int(input_data[1]))
    elif input_data[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif input_data[0] == 'size':
        print(len(stack))
    elif input_data[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif input_data[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)