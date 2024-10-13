import random

def get_user_choice():
    choices = ['камень', 'ножницы', 'бумага']
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    while user_choice not in choices:
        print("Неверный выбор. Попробуйте снова.")
        user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    return user_choice

def get_comp_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and comp_choice == 'ножницы') or \
         (user_choice == 'ножницы' and comp_choice == 'бумага') or \
         (user_choice == 'бумага' and comp_choice == 'камень'):
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"

def play_game():
    user_choice = get_user_choice()
    comp_choice = get_comp_choice()
    print(f"Ваш выбор: {user_choice}")
    print(f"Выбор компьютера: {comp_choice}")
    result = winner(user_choice, comp_choice)
    print(result)

play_game()
