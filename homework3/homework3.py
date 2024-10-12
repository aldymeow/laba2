def input_age(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Введите число.")

def age():
    if d1 >= d and m1 >= m:
        return print ('На сегодняшний день Вам ', y1-y, 'лет')
    else:
        return print('На сегодняшний день Вам ', y1-y-1, 'лет')
                
d = input_age("Введите день вашего рождения (1-31): ")
m = input_age("Введите месяц вашего рождения (1-12): ")
y = input_age("Введите год вашего рождения: ")

d1 = input_age("Введите сегодняшний день (1-31): ")
m1 = input_age("Введите какой сейчас месяц (1-12): ")
y1 = input_age("Введите какой сейчас год: ")

if (1 <= d <= 31) and (1 <= m <= 12) and (1 <= y <= 2024) and (1 <= d1 <= 31) and (1 <= m1 <= 12) and (1 <= y1 <= 2024):
    user_age = age()
    print (user_age)
else:
    print("Необходимо ввести реальные даты")