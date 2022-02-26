class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 50000")

    def withdrawl(self, amount):
        new_amount = 50000 - amount
        print("You have withdrawn amount "+str(amount) +
              ". Your remaining balance is " + str(new_amount))

    def deposit(self, amount):
        new_amount = 50000 + amount
        print("You have amount deposited " + str(amount) +
              "Your balance is " + str(new_amount))


def main():
    Card_number = input("insert your card number:- ")
    pin_number = input("enter your pin number:- ")

    new_user = Atm(Card_number, pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl  3. Deposit")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    elif (activity == 3):
        amount = int(input("enter the amount:- "))
        new_user.deposit(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()
