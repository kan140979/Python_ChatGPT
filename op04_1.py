#Напишите функцию sum_range(start, end), которая суммирует все целые числа от #значения start до величины end включительно.
def sum_range(start, end):
  # Проверяем, что значения start и end целые числа
  if not (isinstance(start, int) and isinstance(end, int)):
      raise ValueError("Оба значения должны быть целыми числами.")

  # Суммируем все целые числа от start до end включительно
  total = sum(range(start, end + 1))
  return total


start = 1
end = 5
result = sum_range(start, end)
print(f"Сумма от {start} до {end} включительно: {result}")