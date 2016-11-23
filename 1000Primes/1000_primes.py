import math


rtn = 5
primes = 3
prime = 5

while primes <= 1000:
    ceil = math.ceil(math.sqrt(prime)) + 1
    is_prime = True
    for i in range(2, ceil):
        if prime % i == 0:
            is_prime = False
            break
    if is_prime:
        primes += 1
        rtn += prime
    prime += 2

print(rtn)
