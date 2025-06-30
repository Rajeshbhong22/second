print("this is june month after june this is not considred")
print("welcome to electricity bill payment website, save electricity, save future")
print("Deadline of the electricity bill payment is 30 june 2025")
print("pay the payment before dead line, after deadline payment fine will be 200rs")
print("hope you are payment done before dead line, Thank You!")
name=input("enter your name:")
date=int(input("enter your date payment:"))
if name=="rajesh":
    total_units=int(input("enter your total units:" ))
    bill=total_units*15
    print("Total bill of the payment:",bill,"rs")
    if 1<=date<=29:
        bill_payment=total_units*15
        print("your total bill is:", bill_payment)
    else:
        fine_bill=(total_units*15)+200
        print("your pay after dead line so, 200rs fine added in you regular bill payment:",fine_bill)
else:
    print("invalid name")


    