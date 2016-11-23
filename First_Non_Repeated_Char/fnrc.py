import sys

for line in open(sys.argv[1]):
    used = []
    excluded = []
    for c in line:
        if c not in used and c not in excluded:
            used.append(c)
        elif c in used:
            used.remove(c)
            excluded.append(c)
    print(used[0])
