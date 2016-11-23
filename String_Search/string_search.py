import sys


def remove_before(longer, shorter):
        for i in range(len(longer)):
            if longer[i] == shorter[0]:
                match = False
                if len(shorter) + i <= len(longer):
                    for j in range(len(shorter)):
                        if shorter[j] != longer[i + j]:
                            match = False
                            break
                        else:
                            match = True
                if match:
                    break_point = i + len(shorter)
                    return longer[break_point-1:]
        return None


file = open(sys.argv[1])
for line in file:
    line = line[:-1]
    longer, tmp = line.split(',')
    shorter = []
    i = 0

    while tmp != "" and i < len(tmp):
        if tmp[i] == '*' and tmp[i-1] != '\\':
            shorter.append(tmp[:i])
            tmp = tmp[i+1:]
        i += 1

    if tmp != "":
        shorter.append(tmp)

    shorter_copy = []
    for item in shorter:
        tmp = None
        for i in range(len(item)-1):
            if item[i:i+2] == "\*":
                tmp = item[:i] + "*"
        if tmp is not None:
            shorter_copy.append(tmp)
        else:
            shorter_copy.append(item)

    shorter = shorter_copy

    fail = False

    for item in shorter:
        if item != "":
            tmp = remove_before(longer, item)
            if tmp is None:
                fail = True
                break
            else:
                longer = tmp

    if fail:
        print("false")
    else:
        print("true")
