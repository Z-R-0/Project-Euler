import math

found = False
n = 7

while found == False:
    #triangle number formula
    x = n/2*(n + 1)
    print(x)

    #count factors
    count = 0
    factors = []
    for i in range(1, int(math.sqrt(x) + 1)):
        if x % i == 0:
            factors.append(i)
            count = count + 1

    if factors[-1]*2 == x:
        a = len(factors) - 2
        count = count + a
    else:
        b = len(factors) - 1
        count = count + b

    if count >= 500:
        print('first triangle number to have over five hundred divisor')
        print(x)
        break

    n = n + 1