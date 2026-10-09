import time

def power(a, n):
    if n == 0: return 1
    return a * power(a, n - 1)

def sum_digits(number):
    number = abs(number)
    return number if number < 10 else number % 10 + sum_digits(number // 10)

def binary_search(array, target, left=0, right=None):
    right = len(array) - 1 if right is None else right
    if left > right: return -1
    middle = (left + right) // 2
    if array[middle] == target: return middle
    if target < array[middle]: return binary_search(array, target, left, middle - 1)
    return binary_search(array, target, middle + 1, right)

def find_max(array):
    if len(array) == 1: return array[0]
    middle = len(array) // 2
    return max(find_max(array[:middle]), find_max(array[middle:]))

def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def tail_fibonacci(n, first=0, second=1):
    if n == 0: return first
    return tail_fibonacci(n - 1, second, first + second)

def deep_flatten(items):
    result = []
    for item in items:
        result.extend(deep_flatten(item) if isinstance(item, list) else [item])
    return result

print(power(2, 5), sum_digits(12345), binary_search([1, 3, 5, 7], 5), find_max([4, 8, 2]))
start = time.perf_counter(); fibonacci(35); print(time.perf_counter() - start)
print(tail_fibonacci(35), deep_flatten([1, [2, [3, 4]], 5]))
