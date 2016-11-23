import sys


def remove_index(s, i):
    if i > len(s) - 1:
        print("remove index error")
    if i == 0:
        return s[1:]
    elif i == len(s)-1:
        return s[:-1]
    else:
        return s[:i] + s[i+1:]


def partition(array, lo, hi):
    pivot = array[hi]
    ip = lo
    for jp in range(lo, hi):
        if array[jp] < pivot: # equiv to array[j] <= pivot
            array[ip], array[jp] = array[jp], array[ip]
            ip += 1
    array[hi], array[ip] = array[ip], array[hi]
    return ip


def quick_sort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quick_sort(array, lo, p - 1)
        quick_sort(array, p + 1, hi)


def gen_perms(string):
    if len(string) == 1:
        return [string]
    else:
        rtn = []
        for i in range(len(string)):
            tmp = remove_index(string, i)
            tmp2 = gen_perms(tmp)
            for item in tmp2:
                rtn.append(string[i] + item)
        return rtn


def main():
    for line in open(sys.argv[1]):
        if line[0] != '\n':
            if line[-1] == '\n':
                line = line[:-1]
            tmp = gen_perms(line)
            perms = [x for x in tmp if len(x) == len(line)]

            quick_sort(perms, 0, len(perms) - 1)
            print(",".join(perms))


if __name__ == "__main__":
    main()
    