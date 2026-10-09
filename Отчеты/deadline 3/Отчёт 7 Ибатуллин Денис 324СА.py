from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class Product:
    name: str
    price: float
    weight: float
    is_available: bool = True
    def order_cost(self, quantity): return self.price * quantity

class Employee:
    def __init__(self, name, salary=0): self.name, self._salary = name, salary
    @property
    def salary(self): return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0: raise ValueError("Зарплата не может быть отрицательной")
        self._salary = value

class StringUtils:
    @staticmethod
    def invert(text): return text[::-1]
    @staticmethod
    def normalize(text): return " ".join(text.split()).lower()
class User:
    def __init__(self, name, role): self.name, self.role = name, role
    @classmethod
    def from_string(cls, value): return cls(*value.split(";"))

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount): pass
    @abstractmethod
    def refund(self, amount): pass
class CreditCardPayment(PaymentSystem):
    def pay(self, amount): return True
    def refund(self, amount): return True
class PayPalPayment(CreditCardPayment): pass

class LoggableMixin:
    def log(self, message): print(f"[LOG] {message}")
class LoggedEmployee(LoggableMixin, Employee): pass

class DatabaseConfig:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None: cls._instance = super().__new__(cls)
        return cls._instance

class Vector3D:
    __slots__ = ("x", "y", "z")
    def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z

class SnakeCaseMeta(type):
    def __new__(mcls, name, bases, namespace):
        for method in namespace:
            if not method.startswith("__") and any(char.isupper() for char in method):
                raise TypeError(f"Имя {method} должно быть snake_case")
        return super().__new__(mcls, name, bases, namespace)
