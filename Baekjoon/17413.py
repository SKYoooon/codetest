import sys

input_data = sys.stdin.readline().strip()

result = []
temp = []
in_tag = False

for char in input_data:
    if char == '<':
        while temp:
            result.append(temp.pop())
        in_tag = True
        result.append(char)
    elif char == '>':
        in_tag = False
        result.append(char)
    elif in_tag:
        result.append(char)
    elif char == ' ':
        while temp:
            result.append(temp.pop()) 
        result.append(' ') 
    else: 
        temp.append(char)

while temp:
    result.append(temp.pop())

print(''.join(result))
