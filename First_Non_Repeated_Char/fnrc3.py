import sys

for line in open(sys.argv[1]):
    used = []
    length = len(line)
    for i in range(length):
        if line[i] not in used:
            if i == length or line[i] not in line[i+1:]:
                print(line[i])
                break
            used.append(line[i])