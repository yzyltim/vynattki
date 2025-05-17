korystuvachi = {
    "Олег": "Дорослий",
    "Марія": "Підліток",
    "Андрій": "Дорослий",
    "Ірина": "Дитина",
    "Софія": "Підліток"
}

imya = input("Введіть ім'я користувача: ")

try:
    vikova_grupa = korystuvachi[imya]
    print(f"{imya} належить до вікової групи: {vikova_grupa}")
except KeyError:
    print(f"Помилка: користувача з іменем '{imya}' не знайдено.")
