def get_number():
    for number in range(30):
        if number % 2 != 0:
            yield number

def main():
    generator = get_number()
    
    first = None
    fifth = None
    last = None
    
    for index, value in enumerate(generator, start=1):
        if index == 1:
            first = value
        if index == 5:
            fifth = value
        last = value 
    print(f"Пятое нечетное число: {fifth}")
    print(f"Последнее нечетное число: {last}")

if __name__ == "__main__":
    main()
