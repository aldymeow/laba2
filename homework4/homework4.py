import random

def find_multiples(x):
    multiples = []
    while len(multiples) < 10:
        n = random.randint(0, 200)
        if n % x == 0:
            multiples.append(n)
    return multiples

def main():
    try:
        x = int(input("Введите число X (от 1 до 9): "))
        if x < 1 or x > 9:
            print("Пожалуйста, введите цифру от 1 до 9.")
            return
    except ValueError:
        print("Пожалуйста, введите целое число.")
        return

    result = find_multiples(x)
    print(f"Числа, кратные {x}: {result}")


main()
