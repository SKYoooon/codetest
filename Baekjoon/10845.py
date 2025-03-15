import sys
num_count = int(sys.stdin.readline())
queue = []

for _ in range(num_count):
    input_data = sys.stdin.readline().split()
    command = input_data[0]
    if command == 'push':
        queue.append(int(input_data[1]))
    elif command == 'pop':
        print(queue.pop(0) if queue else -1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(0 if queue else 1)
    elif command == 'front':
        print(queue[0] if queue else -1)
    elif command == 'back':
        print(queue[-1] if queue else -1)