# 1
grades = [float(input()) for _ in range(5)]
print(grades)
grades.pop(0); grades.pop()
print(sum(grades) / len(grades), grades)

# 2
numbers = [1, 17, 24, 35, 48, 51, 62, 73, 86, 99]
print([x for x in numbers if x % 2 == 0])
print([x for x in numbers if x > 50])

# 3
tasks = []
while True:
    command = input("show/add/delete/exit: ")
    if command == "show":
        for index, task in enumerate(tasks, 1): print(index, task)
    elif command == "add": tasks.append(input())
    elif command == "delete": tasks.pop(int(input()) - 1)
    elif command == "exit": break

# 4
celsius = [12, 15, 10, 18, 20, 17, 14, 9, 11, 16, 22, 19, 13, 8]
average = sum(celsius) / len(celsius)
print(max(celsius), min(celsius), average, sum(x > average for x in celsius))
print(sorted(celsius), [x * 9 / 5 + 32 for x in celsius])

# 5
import re
words = re.findall(r"[а-яёa-z]+", input().lower())
counts = {word: words.count(word) for word in set(words)}
print(max(words, key=len), min(words, key=len), sum(map(len, words)) / len(words))
print(sorted(counts, key=counts.get, reverse=True)[:5])

# 6
board = [[" "] * 3 for _ in range(3)]
for turn in range(9):
    mark = "X" if turn % 2 == 0 else "O"
    row, column = map(int, input("Строка столбец: ").split())
    if board[row][column] != " ": continue
    board[row][column] = mark
    print(*("|".join(line) for line in board), sep="\n")
    lines = board + list(zip(*board)) + [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    if any(all(cell == mark for cell in line) for line in lines):
        print(mark, "победил"); break
else: print("Ничья")
