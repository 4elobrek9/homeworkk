import math

a = int(input("Введите сумму депозита: "))
b = int(input("Введите баланс: "))
c = int(input("Введите депозит (если 0, то будет ставка средняя по миру): "))


class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # Приватный атрибут

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance


account = BankAccount(b)
account.deposit(a)

# Установка ставки депозита
if c == 0:
    depoz = 17.63
else:
    depoz = c

# Расчет будущего баланса
future = account.get_balance() * (1 + depoz / 100)  # Учитываем процент
mew = round(future)
plus = mew - account.get_balance()

print(f"\nНа вашем депозитном счету: {account.get_balance()}")  # Вывод текущего баланса

# Вывод будущего баланса через год
print(f"\nЧерез год ваш баланс будет составлять (по средней депозитной ставке: 17,63%): {mew}")
print(f"прибыль составила: {plus}")