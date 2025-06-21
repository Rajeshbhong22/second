menu={ 'pizza': 40,
       'pasta': 50,
       'poha' : 20,
       'noodles': 100,
       'paratha': 50,
       'tea'   : 10,
       'coffee': 80
       
}

print("welcome to rajesh restaurent")
print("pizza: 40rs\npasta:50rs\npoha:20rs\nnoodles:100rs\nparatha:50rs\ntea:10rs\ncoffee:80rs")
order_total=0

item_1=input('enter the name of item you want to order=')
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has beem added to your order")
else:
    print("this {iteM_1} is not avalible now")
    
anther_order=input(" Yoru want anything else (yes/no):")
if anther_order=='yes':
   item_2=input("what you want another item:")
   if item_2 in menu :
       order_total+=menu[item_2]
   else:
    print(f"this order{item_2}is not avaliable now")

print("your total amount to pay", order_total)

