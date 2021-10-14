class Account:
    def __init__(self):
        pass
    def show(self):
        print(f"name: {self.name} account number:{self.number} balace: {self.balance}")

my_account=Account ()
my_account.name="shlomi"
my_account.number=985485
my_account.balance=5000

my_account.show()