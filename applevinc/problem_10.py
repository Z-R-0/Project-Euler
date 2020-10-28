import math

sum = 0

def is_prime(n):

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    else:
        return True

for n in range(2, 2000000):

    if is_prime(n):
        print(n)
        sum = sum + n

print(sum)


