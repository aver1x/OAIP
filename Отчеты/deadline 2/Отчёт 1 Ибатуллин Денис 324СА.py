# 1
number = int(input())
total = 0
while number:
    total += number % 10
    number //= 10
print(total)

# 2
count = 0
while True:
    number = int(input())
    if number == 0:
        break
    count += 1
print(count)

# 3
text = "".join(input().lower().split())
left, right = 0, len(text) - 1
is_palindrome = True
while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print(is_palindrome)

# 4
import random
secret = random.randint(1, 100)
while True:
    guess = int(input())
    if guess == secret:
        print("Угадано")
        break
    print("Больше" if guess < secret else "Меньше")

# 5
vowels = "аеёиоуыэюяaeiou"
text = input()
index, result = 0, ""
while index < len(text):
    if text[index].lower() not in vowels:
        result += text[index]
    index += 1
print(result)

# 6–7
symbol = input()
height, width = map(int, input().split())
row = 0
while row < height:
    column, line = 0, ""
    while column < width:
        line += symbol if row in (0, height - 1) or column in (0, width - 1) else " "
        column += 1
    print(line)
    row += 1
