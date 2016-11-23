import sys


file = open(sys.argv[1])
for line in file:
    if line[-1] == '\n':
        line = line[:-1]

    n, m, nums = line.split(';')
    nums_list = nums.split(' ')

    rtn = []

    top = 0
    left = 0
    right = int(m)
    bottom = int(n)
    index = 0
    added = 0
    limit = right * bottom

    matrix = []
    for i in range(bottom):
        tmp = []
        for k in range(right):
            tmp.append(nums_list[index])
            index += 1
        matrix.append(tmp)

    while True:
        for i in range(left, right):
            rtn.append(matrix[top][i])
            added += 1
        top += 1

        if added == limit:
            break

        for i in range(top, bottom):
            rtn.append(matrix[i][right - 1])
            added += 1
        right -= 1

        if added == limit:
            break

        for i in reversed(range(left, right)):
            rtn.append(matrix[bottom - 1][i])
            added += 1
        bottom -= 1

        if added == limit:
            break

        for i in reversed(range(top, bottom)):
            rtn.append(matrix[i][left])
            added += 1
        left += 1

        if added == limit:
            break

    print(" ".join(rtn))
