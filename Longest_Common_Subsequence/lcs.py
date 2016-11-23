import sys

file = open(sys.argv[1])
for line in file:
    if line[0] != '\n':
        first, second = line.split(';')
        x = len(first) + 1
        y = len(second) + 1
        matrix = [["" for j in range(y)] for i in range(x)]
        largest_val = 0
        largest_str = None
        for i in range(x):
            for j in range(y):
                if first[i-1] == second[j-1]:
                    if i > 0 and j > 0:
                        matrix[i][j] = matrix[i-1][j-1] + first[i-1]
                        tmp = len(matrix[i][j])
                        if tmp > largest_val:
                            largest_val = tmp
                            largest_str = matrix[i][j]

                else:
                    if i > 0 and j > 0:
                        if len(matrix[i-1][j]) > len(matrix[i][j-1]):
                            matrix[i][j] = matrix[i-1][j]
                        else:
                            matrix[i][j] = matrix[i][j-1]

        print(largest_str)
