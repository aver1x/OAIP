from functools import wraps
from time import perf_counter

def create_counter():
    value = 0
    def counter():
        nonlocal value
        value += 1
        return value
    return counter

def make_bold(function):
    @wraps(function)
    def wrapper(*args, **kwargs): return f"<b>{function(*args, **kwargs)}</b>"
    return wrapper

def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print(function.__name__, args, kwargs, result)
        return result
    return wrapper

def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter(); result = function(*args, **kwargs)
        print("Время:", perf_counter() - start)
        return result
    return wrapper

def safe_exec(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try: return function(*args, **kwargs)
        except ZeroDivisionError:
            print("Деление на ноль")
            return 0
    return wrapper

def repeat(count):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count): result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator

counter = create_counter()
print(counter(), counter())
