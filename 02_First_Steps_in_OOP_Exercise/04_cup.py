# Exam: 04. Cup
# From: First Steps in OOP - Exercise
# URL: https://judge.softuni.org/Contests/Practice/Index/1935#3

class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        self.quantity += amount if self.status() >= amount else 0

    def status(self):
        return self.size - self.quantity


# Test code
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
