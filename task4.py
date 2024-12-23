import threading
import random
import time

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited: {amount}, New balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn: {amount}, New balance: {self.balance}")
            else:
                print(f"Failed to withdraw {amount}, insufficient balance")

def client_transactions(account):
    for _ in range(5):
        action = random.choice(["deposit", "withdraw"])
        amount = random.randint(1, 100)
        if action == "deposit":
            account.deposit(amount)
        elif action == "withdraw":
            account.withdraw(amount)
        time.sleep(random.uniform(0.1, 0.5))

account = BankAccount(1000)

threads = []
for _ in range(5):
    t = threading.Thread(target=client_transactions, args=(account,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final balance: {account.balance}")
