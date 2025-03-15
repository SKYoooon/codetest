import sys

num_count = int(sys.stdin.readline())

for _ in range(num_count):
    input_data = sys.stdin.readline().strip()
    left_count = 0
    is_matched = True
    
    for i in input_data:
        if i == '(':
            left_count += 1
        elif i == ')':
            left_count -= 1

        if left_count < 0:
            is_matched = False
            break


    if left_count == 0 and is_matched:
        print('YES')
    else:
        print('NO')
