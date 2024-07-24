#Напишите свою собственную игру - камень ножницы бумага Игра должна идти до 3-х побед,
#и выводить кто победил

import random


def get_user_choice():
    user_input = input("Введите 'камень', 'ножницы' или 'бумага': ").lower()
    while user_input not in ['камень', 'ножницы', 'бумага']:
        print("Некорректный ввод. Попробуйте снова.")
        user_input = input(
            "Введите 'камень', 'ножницы' или 'бумага': ").lower()
    return user_input


def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'ничья'
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return 'игрок'
    else:
        return 'компьютер'


def main():
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        print("\nТекущий счет - Игрок: {}, Компьютер: {}".format(
            user_score, computer_score))
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("Вы выбрали:", user_choice)
        print("Компьютер выбрал:", computer_choice)

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'игрок':
            print("Вы выиграли раунд!")
            user_score += 1
        elif winner == 'компьютер':
            print("Компьютер выиграл раунд!")
            computer_score += 1
        else:
            print("Это ничья!")

    if user_score == 3:
        print("\nПоздравляем! Вы победили!")
    else:
        print("\nКомпьютер победил! Лучше повезет в следующий раз.")


if __name__ == "__main__":
    main()
