import sys

file = open(sys.argv[1])
for line in file:
    if line[-1] == '\n':
        line = line[:-1]

    my_list = line.split(' ')
    my_list.reverse()
    stack = []

    for item in my_list:
        if item.isdigit():
            stack.append(int(item))
        elif item == "+":
            num1 = stack.pop(-1)
            num2 = stack.pop(-1)
            stack.append(num1 + num2)
        elif item == "*":
            num1 = stack.pop(-1)
            num2 = stack.pop(-1)
            stack.append(num1 * num2)
        elif item == "/":
            num1 = stack.pop(-1)
            num2 = stack.pop(-1)
            stack.append(num1 / num2)

    print(int(stack[-1]))
