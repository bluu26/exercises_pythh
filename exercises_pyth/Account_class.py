class Account:

    def __init__(self, numer, stan):
        self.numer = numer
        self.stan = stan


    def deposit(self, amount):
        self.stan += amount

    def withdraw(self, amount):
        if amount > 0:
            self.stan -= amount