import sys

num_of_input = int(sys.stdin.readline())

for _ in range(num_of_input):
    sentence = sys.stdin.readline().split()

    reversed_word = []
    
    for word in sentence:
        reversed_word.append(word[::-1])
    
    print(" ".join(reversed_word))
