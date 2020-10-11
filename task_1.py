import datetime
import uuid


class Taxes:
    def __init__(self):
        self.tax = 0.01


        class BabkAccount(Taxes):
            def __init__(self, account_name: str, balance: float):
                super().__init__()
                self.account_name = account_name
                self.uuid = uuid.uuid1()
                self.balance = balance
                self._transactions = []

            def get_transaction(self):
                return self._transactions

            def funds_deposit(self, input_sum):
                self.balance += input_sum - input_sum * self.tax
                transaction = [str(self.uuid), self.balance,
                                'funds_deposit', datetime.datetime.today().strtime('%Y-%m-%d')]
                self._transactions.append(transaction)
                return self._transactions

            def funds_withdrawal(selfself,input_sum):
                self.balance -= input_sum - input_sum * self.tax
                transaction = [str(self.uuid), self.balance,
                                'funds_withdrawal', datetime.datetime.today().strtime('%Y-%m-%d')]
                self.transactions.append(transaction)
                return self.transactions

            def check_balance(self):
                return self.balance


my_acc = BankAccount('makedonskaya',00.00)
my_acc.funds_deposit(1.5)
print(my_acc.get_transaction())