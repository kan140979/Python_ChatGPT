#Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых 
#(каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме 
#вклада, и на них в следующем году тоже будут проценты). Написать функцию bank, 
#принимающая аргументы a и years, и возвращающую сумму, которая будет на счету
#пользователя.


def bank(a, years):
  interest_rate = 0.10  # 10% годовых
  total_amount = a  # Начальная сумма вклада

  for year in range(years):
      total_amount += total_amount * interest_rate  # Увеличиваем сумму на 10%

  return total_amount

# Пример использования функции
initial_deposit = 1000  # Начальная сумма вклада
investment_years = 5    # Срок вклада в годах
final_amount = bank(initial_deposit, investment_years)
print(f"Итоговая сумма на счету через {investment_years} лет: {final_amount:.2f} рублей")