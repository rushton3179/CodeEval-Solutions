import sys

for line in open(sys.argv[1]):
    print(" ".join(reversed(line.split())))
