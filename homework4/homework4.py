import random

def find_multiples(x):
    multiples = []
    while len(multiples) < 10:
        n = random.randint(0, 200)
        if n % x == 0:
            multiples.append(n)
    return multiples

x = int(input("Введите число X: "))
print(find_multiples(x))