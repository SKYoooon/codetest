import sys

input_data = str(sys.stdin.readline()).replace('()','L')

stack = []
result = 0

for char in input_data:
    if char == '(':
        stack.append(char)
    elif char == ')':
        stack.pop()
        result += 1
    else:
        result += len(stack)
print(result)