import sys

file = open(sys.argv[1])
for line in file:
    if line[-1] == '\n':
        line = line[:-1]
    print(line.lower())