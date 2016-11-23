import math


found = False
rtn = None

for i in reversed(range(10)):
    for j in reversed(range(10)):
        is_prime = True
        num = int(str(i) + str(j) + str(i))
        sqrt_num = math.ceil(math.sqrt(num))
        for k in range(2, sqrt_num + 1):
            if num % k == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
            found = True

        if found:
            break
    if found:
        break
