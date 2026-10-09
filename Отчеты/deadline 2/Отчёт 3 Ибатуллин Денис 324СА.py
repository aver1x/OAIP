# 1
fruits = {"яблоки": 5, "бананы": 3, "апельсины": 10, "арбузы": 33}
print(fruits)
fruits["яблоки"] -= 2
fruits.pop("арбузы")
print(fruits)

# 2
text = input().lower()
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
print(counts)

# 3
phonebook = {"Анна": "111", "Борис": "222", "Вера": "333"}
while True:
    command = input("show/add/delete/exit: ")
    if command == "show":
        print(*[f"{name}: {phone}" for name, phone in phonebook.items()], sep="\n")
    elif command == "add":
        name, phone = input().split()
        if name not in phonebook: phonebook[name] = phone
    elif command == "delete":
        name = input()
        print("Удален" if phonebook.pop(name, None) else "Не найден")
    elif command == "exit": break

# 4
products = {"Телефон": {"price": 50000, "sold": 4}, "Ноутбук": {"price": 90000, "sold": 2}, "Наушники": {"price": 5000, "sold": 10}}
revenue = {name: item["price"] * item["sold"] for name, item in products.items()}
print(max(products, key=lambda name: products[name]["sold"]))
print(sum(revenue.values()), max(revenue, key=revenue.get))

# 5
import re
statistics = {}
while line := input():
    for word in re.findall(r"[а-яёa-z]+", line.lower()):
        statistics[word] = statistics.get(word, 0) + 1
print(statistics)

# 6
import random
stock = {"яблоки": 20, "бананы": 15, "апельсины": 10}
prices = {"яблоки": 80, "бананы": 100, "апельсины": 120}
money = 5000
for day in range(1, 11):
    for fruit in stock:
        sold = random.randint(0, stock[fruit])
        stock[fruit] -= sold
        money += sold * prices[fruit]
    if random.random() < 0.2:
        for fruit in stock: stock[fruit] //= 2
    print(day, stock, money)
