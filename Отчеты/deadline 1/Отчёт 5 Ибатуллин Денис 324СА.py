# 1
first, second = map(float, input().split())
print(first + second, first - second, first * second, first / second)

# 2
x, y, z = map(int, input().split())
print(x * y, y * z, z * x, x ** 4, y % z, z // x)
print(x ** 4 + y % z + z // x)

# 3
for part in input("ФИО: ").split():
    print(part.upper())

# 4
numbers = [float(value) for value in input().split()]
print(min(numbers), max(numbers))

# 5
import random
import string

def random_text(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(alphabet) for _ in range(length))

message = input("Сообщение: ")
count = int(input("Количество символов: "))
print("".join(char + random_text(count) for char in message))
