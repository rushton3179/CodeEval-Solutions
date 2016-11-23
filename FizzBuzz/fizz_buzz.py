import sys


file = open(sys.argv[1])
for line in file:
    if line[1] != '\n':
        answer = ""
        line_list = line.split()
        fizz = int(line_list[0])
        buzz = int(line_list[1])
        n = int(line_list[2])
        for i in range(1, n+1):
            if i % fizz != 0 and i % buzz != 0:
                tmp = str(i) + " "
                answer += tmp
            elif i % fizz == 0 and i % buzz != 0:
                answer += "F "
            elif i % fizz != 0 and i % buzz == 0:
                answer += "B "
            elif i % fizz == 0 and i % buzz == 0:
                answer += "FB "
        print(answer[:-1])
