# 1
move = input().lower()
actions = {"left": "Иду влево", "right": "Иду вправо", "straight": "Иду прямо", "back": "Иду назад"}
print(actions.get(move, "Неправильное направление"))

# 2
password = input("Пароль: ")
confirmation = input("Подтверждение: ")
print("Access" if password == confirmation else "Denied")

# 3
text = input("Текст: ").lower()
word = input("Слово: ").lower()
print(word in text, text.count(word))

# 4
year = int(input("Год: "))
print("Високосный" if year % 400 == 0 or year % 4 == 0 and year % 100 else "Обычный")

# 5
import math
first, operation, second = input("Число оператор число: ").split()
a, b = float(first), float(second)
if operation == "+": result = a + b
elif operation == "-": result = a - b
elif operation == "*": result = a * b
elif operation == "/": result = a / b
elif operation == "%": result = a % b
elif operation == "//": result = a // b
elif operation == "**": result = a ** b
elif operation == "%%": result = a * b / 100
elif operation == "/**": result = math.sqrt(a)
else: raise ValueError("Неизвестный оператор")
print(result)
