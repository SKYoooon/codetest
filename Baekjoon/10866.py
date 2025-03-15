import sys
num_count = int(sys.stdin.readline())
deque = []

for i in range(num_count):
    input_data = sys.stdin.readline().split()
    cmd = input_data[0]
    if cmd == 'push_front':
        deque.insert(0, int(input_data[1]))
    elif cmd == 'push_back':
        deque.append(int(input_data[1]))
    elif cmd == 'pop_front':
        print(deque.pop(0) if deque else -1)
    elif cmd == 'pop_back':
        print(deque.pop() if deque else -1)
    elif cmd == 'size':
        print(len(deque))
    elif cmd == 'empty':
        print(0 if deque else 1)
    elif cmd == 'front':
        print(deque[0] if deque else -1)
    elif cmd == 'back':
        print(deque[-1] if deque else -1)