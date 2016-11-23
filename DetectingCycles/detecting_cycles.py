import sys


file = open(sys.argv[1])
for line in file:
    if line[-1] == '\n':
        line = line[:-1]

    seq = line.split(" ")
    n = len(seq)

    start = None
    end = None
    i = 0
    while start is None:
        for j in range(i + 1, n):
            if seq[j] == seq[i]:
                tmp = i
                tmp2 = j
                while tmp < j and tmp2 < n and seq[tmp] == seq[tmp2]:
                    tmp += 1
                    tmp2 += 1

                if tmp2 == len(seq) or tmp == j:
                    start = i
                    end = j
                    break
        i += 1

    if start is not None:
        print(" ".join(seq[start:end]))
