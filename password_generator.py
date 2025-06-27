import random

# Определение наборов символов
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
ambiguous_chars = "il1Lo0O"

# Функция для получения проверенного ввода от пользователя
def get_input(prompt, input_type=int):
    while True:
        try:
            value = input_type(input(prompt))
            if input_type == int and value > 0:
                return value
            elif input_type == str and value in ("да", "нет"):
                return value
            else:
                print("Неверный ввод! Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод! Пожалуйста, попробуйте снова.")

# Получение данных от пользователя с проверками
pwd_quantity = get_input("Укажите количество паролей для генерации: ")
pwd_len = get_input("Укажите длину одного пароля: ")
pwd_digits = get_input("Включать ли цифры 0123456789? (да/нет) ", str)
pwd_uppercase = get_input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет) ", str)
pwd_lowercase = get_input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет) ", str)
pwd_punctuation = get_input("Включать ли символы !#$%&*+-=?@^_? (да/нет) ", str)
pwd_exceptions = get_input("Исключать ли неоднозначные символы il1Lo0O? (да/нет) ", str)

# Генерация набора символов на основе пользовательских предпочтений
def get_characters():
    chars = ""
    if pwd_digits == "да":
        chars += digits
    if pwd_uppercase == "да":
        chars += uppercase_letters
    if pwd_lowercase == "да":
        chars += lowercase_letters
    if pwd_punctuation == "да":
        chars += punctuation
    if pwd_exceptions == "да":
        for c in ambiguous_chars:
            chars = chars.replace(c, "")
    return chars

# Функция генерации пароля
def generate_password(length, chars):
    return "".join(random.choices(chars, k=length))

# Основной цикл для генерации паролей
chars = get_characters()
if chars:
    for _ in range(pwd_quantity):
        print(generate_password(pwd_len, chars))
else:
    print("Нет доступных символов для создания пароля. Проверьте настройки.")
