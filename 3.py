try:
    file_path = input("Введіть шлях до файлу: ")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Вміст файлу:")
        print(content)
except FileNotFoundError:
    print("Помилка: файл не знайдено. Перевірте шлях.")
