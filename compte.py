import random


class Compte:
    def __init__(self, client, balance, username, password):
        self.client = client
        self.account_number = self.generate_account_number()
        self.balance = balance
        self.username = username
        self.password = password
        self.is_authentified = False

    def generate_account_number(self):
        return f'CMP_{self.client.firstname[:4]}_{random.randint(100,900)}'

    def log_in(self, username, password):
        if self.username == username and self.password == password:
            self.is_authentified = True

    def log_out(self):
        self.is_authentified = False

    def retrait_argent(self, amount):
        if self.is_authentified:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise Exception('votre solde ne suffit pas')
        else:
            raise Exception(
                'vous pouvez pas faire le retrait, veuillez connectera votre compte svp!')

    def deposer_argent(self, amount):
        if self.is_authentified:
            self.balance += amount
        else:
            raise Exception(
                'vous pouvez pas faire le retrait, veuillez connectera votre compte svp!')

    def __str__(self):
        return f'Compte: {self.account_number} a: {self.balance} euros'
