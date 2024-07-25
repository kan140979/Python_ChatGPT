"""Задание 2: Обработка множества видов исключений
Напиши программу, которая запрашивает у пользователя ввести целое число, а затем пытается преобразовать введенное значение в целочисленный тип. Используй блок try-except, чтобы корректно обработать возможные исключения, которые могут возникнуть в этом процессе, включая ValueError. В случае ValueError выведи сообщение "Невозможно преобразовать введенное значение в целое число". Программа должна просить пользователя попробовать ввести число еще раз. Убедись, что программа корректно работает с корректным вводом, и продемонстрируй ее поведение на некорректном вводе."""


while True:
  user_input = input("Введите целое число: ")
  try:
      number = int(user_input)  
      print(f"Вы ввели число: {number}")
      break  
  except ValueError:
      print("Невозможно преобразовать введенное значение в целое число. Попробуйте снова.")