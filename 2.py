try:
    user_input = input("Введіть число: ")
    number = int(user_input)
    print(f"Ви ввели число: {number}")
except ValueError:
    print("Помилка: введене значення не є цілим числом.")
