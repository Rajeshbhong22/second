class ATM:
    def __init__(self):
        self.balance=1000
        self.pin=int(input("enter your pin:"))
        self.opr="y"
        if self.pin==12345:
            print("1.widraw_money\n2.deposite_money\n3.check_balance\n4.pin_change")
            choice=int(input("enter your choice:"))
a1=ATM