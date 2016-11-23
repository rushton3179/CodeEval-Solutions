import sys
import heapq


file = open(sys.argv[1])
first = True
num = None
heap = []
for line in file:
    if line[-1] == '\n':
        line = line[:-1]
    if first:
        num = int(line)
        first = False
    else:
        if len(heap) < num:
            heapq.heappush(heap, (len(line), line))
        elif heap[0][0] <= len(line):
            heapq.heapreplace(heap, (len(line), line))

tmp = []
while heap:
    tmp.append(heapq.heappop(heap)[1])
for item in reversed(tmp):
    print(item)