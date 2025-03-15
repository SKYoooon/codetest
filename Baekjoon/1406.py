import sys

word = list(sys.stdin.readline().strip())
num_count = int(sys.stdin.readline())

word_left = word
word_right = []

for _ in range(num_count):
    command = sys.stdin.readline().strip()

    if command[0] == 'L' and word_left:
        word_right.append(word_left.pop())
    elif command[0] == 'D' and word_right:
        word_left.append(word_right.pop())
    elif command[0] == 'B' and word_left:
        word_left.pop()
    elif command[0] == 'P':
        word_left.append(command[2]) #command[1] == ' '
print(''.join(word_left + (word_right[::-1])))