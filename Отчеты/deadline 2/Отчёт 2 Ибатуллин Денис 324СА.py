# 1
n = int(input())
print(sum(range(1, n + 1)))

# 2
n = int(input())
for multiplier in range(1, 11):
    print(f"{n} * {multiplier} = {n * multiplier}")

# 3
text = input()
letters = digits = punctuation = spaces = 0
for char in text:
    letters += char.isalpha()
    digits += char.isdigit()
    punctuation += char in ".,!?:;"
    spaces += char.isspace()
print(letters, digits, punctuation, spaces)

# 4
n = int(input())
for row in range(1, n + 1):
    print(" ".join(str(number) for number in range(1, row + 1)))

# 5
numbers = [float(value) for value in input().split()]
average = sum(numbers) / len(numbers)
print(max(numbers), min(numbers), average)
print(sum(number > average for number in numbers))

# 6
n = int(input())
spiral = [[0] * n for _ in range(n)]
x = y = n // 2
spiral[y][x] = 1
value, step = 2, 1
while value <= n * n:
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        for _ in range(step):
            if value > n * n: break
            x, y = x + dx, y + dy
            spiral[y][x] = value
            value += 1
        if dx == 0: step += 1
for row in spiral: print(*row)
