# print("welcome to hdfc atom, ham tyar hai apke seva mai 24/7")
# import time
# balance=1000
# card=print("Insert your card in the atm:")
# time.sleep(5)
# pin=int(input("enter you pin:"))
# if pin==123456:
#     print( "1 widraw money\n2 deposite money\n3 check balance\n4 change pin\n5 exite")
#     select_option=int(input("selec one the option given:"))
#     if select_option==1:   
#         insert_bal=int(input("enter your amount:"))  
#         if insert_bal>balance:
#             print("insufficient balance")
#         else:
#             balance-=insert_bal
#             print("balance amount is:",balance)
#             print("thank YOu!, transiction successfully")
#     elif select_option==2:
#         add_amount=int(input("add your amount in the account:"))
#         total_amount=balance+add_amount
#         print("total balance in the account is:",total_amount)
#     elif select_option==3:
#         print("account balance is",balance)
#     elif select_option==4:
#         new_pin=int(input("enter your new pin:"))
#         pin=new_pin
#         print("your new pin is",pin)
#     elif select_option==5:
#         print("exit")
# else:
#     print("invalid pin")



import time
    
class ATM:
    def __init__(self):
        print("insert your card in ATM")
        time.sleep(5)
        self.balance=1000
        self.pin=int(input("enter your pin:"))
        self.opr="y"
        if self.pin==12345:
            while self.opr=="y":
                print("1.widraw_money\n2.deposite_money\n3.check_balance\n4.pin_change")
                choice=int(input("enter your choice"))
                if choice==1:
                    self.widraw_money()
                    self.opr=input("Do you want to contiue?(y or n): ")
                elif choice==2:
                    self.deposite_money()
                    self.opr=input("Do you want to contiue?(y or n): ")
                elif choice==3:
                    self.check_balance()
                    self.opr=input("Do you want to contiue?(y or n): ")
                elif choice==4:
                    self.pin_change()
                    
                    
                else:
                    print("invalid choice")
                    self.opr=input("do you want to contiue?")
        else:
            print("invalid pin")

    def widraw_money(self):
        money=int(input("enter your amount you want to widraw:"))
        self.balance-=money
        print("Your widrawal is succesful,Your balance is:",self.balance)
    def deposite_money(self):
        money=int(input("enter your deposite amount:"))
        self.balance+=money
        print("Your deposite added in the balance:", self.balance)
    def check_balance(self):
        print("Your balance is:", self.balance)
    def pin_change(self):
        new_pin=int(input("enter your new pin:"))
        self.pin=new_pin
        
        if self.pin==new_pin:
                self.opr=input("do you want to continue?(y or n):")
                self.pin=int(input("enter your pin:"))
                
                      

a1=ATM()

