#Написать конвертер валюты. Эта программа будет конвертировать введённую пользователем
#сумму в другую валюту. Курс валюты можно ввести самостоятельно и один раз.


def currency_converter():
    print("Добро пожаловать в конвертер валюты!")

    # Ввод курса валюты
    currency_rate = float(
        input("Введите курс валюты (например, 0.85 для доллара в евро): "))

    while True:
        try:
            # Ввод суммы для конвертации
            amount = float(
                input(
                    "Введите сумму для конвертации (или 'exit' для выхода): "))
            converted_amount = amount * currency_rate
            print(f"Конвертированная сумма: {converted_amount:.2f}")
        except ValueError:
            print("Вы вышли из программы.")
            break


if __name__ == "__main__":
    currency_converter()
