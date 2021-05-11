# Write a python program to create a bank class where deposits and withdrawal can be 
# handled by using instance methods.

class Account:
    def __init__(self):
        self.balance = 0
        print("Your Account has been initialized")

    def deposits(self):
        amount=int(input('Enter the amount to deposit:'))
        self.balance+=amount
        print(f"Your New Balance is {self.balance}")
    def withdrawal(self):
        amount=int(input('Enter the amount to withdraw:'))
        if amount> self.balance:
            print("You dont to enough balance!")
            print(f'Your Balance is {self.balance}')
        else:
            self.balance -= amount
            print(f"Your New Balance is {self.balance}")
    def balance_enquiry(self):
        print(f'Your Balance is {self.balance}')

acc = Account()
acc.deposits()
acc.withdrawal()
acc.balance_enquiry()