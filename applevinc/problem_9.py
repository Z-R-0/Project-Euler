import math

sum = 1000

for a in range(1, int(sum/3)):
    #print(a)
    for b in range(int(sum/3) + 1, int(sum/2)):

        num = a**2 + b**2
        c = math.sqrt(num)


        if a + b + c == sum:
            product = a*b*c
            print(product)
            break



