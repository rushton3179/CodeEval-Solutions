import sys

for line in open(sys.argv[1]):
    length = len(line)
    for i in range(length):
        answer = None
        has_double = False
        j = 0
        while not has_double and j < (length + 1):
            if j == length:
                answer = line[i]
            elif line[i] == line[j] and i != j:
                has_double = True
            j += 1

        if answer is not None:
            print(answer)
            break
