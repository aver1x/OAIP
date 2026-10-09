# 1
fio = " ".join(part.capitalize() for part in input("ФИО: ").split())
print("Здравствуйте,", fio)

# 2
text = input("Текст: ")
old, new = input("Старая и новая строка: ").split()
print(text.replace(old, new))

# 3
text = input("Текст: ")
step = int(input("Шаг: "))
print(text[::step])

# 4
text = input("Текст: ")
start, end = map(int, input("Начало и конец: ").split())
print(text[start - 1:end])

# 5
text = input("Текст: ")
word = input("Слово: ")
print(text.count(word))
print(text.find(word))
print(text.replace(word, ""))
