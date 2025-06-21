

# # #product calcul

# # p=int(input("enter1:"))
# # intr=int(input("enter2:"))
# # yer=int(input("enter3:"))
# # simple_interest=(p*yer*intr)/100
# # print(simple_interest)
# # threshold_amount=120000
# # check=simple_interest>=threshold_amount
# # print("comparison",check)

# #float function
# # a=20
# # print(a)
# # print(type(a))
# # c=float(a)
# # print(c)
# # print(type(c))

# #eample no 2
# # a="3.14"
# # print(a)
# # print(type(a))
# # c=float(a)
# # print(c)
# # print(type(c))

# # int finction

# # player_score=300.52
# # inter_score=int(player_score)
# # print(inter_score)

# #simple interest
# # p=100025.4554
# # n=3.5
# # rate=10
# # simple_interest=(p*n*rate)/100
# # print("actual interst in float also:",simple_interest)
# # print("simple interest is:", int(simple_interest))


# #binary function= which converts ordinary number into binary digits or number

# # z=5
# # print(bin(z))
# # z=500
# # print(bin(z))

# #sum finction 
# # l=[1,2,3,4,5]
# # start_no= 40
# # print(sum(l,start_no))

# #eval function

# # x=10
# # y=14
# # exp="x+y+y*x*y/y"
# # print(eval(exp))

# # name1=input("enter your name:")
# # name2=input("enter your name:")

# # print("welcome",name1)
# # print("welcome", name2)

# # a=float(input("enter the value:"))
# # b=int(input("enter the value:"))
# # sum=a+b
# # print('sum is',sum)


# # age=float(input("enter the age:"))
# # weight=float(input("enter the weight:"))
# # height=float(input("enter your height"))

# # bmr=(88.362+(13.397*abs(weight))+(4.799*abs(height))-(5.677*abs(age)))
# # print('bmr of person is:',bmr)
# # print("bmr in integer is given by")
# # print(int(bmr))




# # age_student1=int(input("enter your age"))
# # age_student2=int(input("enter your age:"))
# # age_student3=int(input("enter your age:"))
# # age_student4=int(input("enter your age:"))
# # age_student5=int(input("enter your age:"))
# # stu1_course=input("enter your course")
# # stu2_course=input("enter your course")
# # stu3_course=input("enter your course")
# # stu4_course=input("enter your course")
# # stu5_course=input("enter your course")
# # print("student1",stu1_course,age_student1)
# # print("student2",stu2_course,age_student2)
# # print("student3",stu3_course,age_student3)
# # print("student4",stu4_course,age_student4)
# # print("student5",stu5_course,age_student5)

# # sum_age=(age_student5+age_student4+age_student3+age_student2+age_student1)
# # agverage_age=sum_age/5

# #we are solving question, determine current temperture within the minimum temp and maximum temp

# # current_temperature=int(input("enter the current temp.:"))
# # minimum_temperture=int(input("enter the minumum temp:"))
# # maximum_tempeture=int(input('enter the maximum temp:'))

# # compare_temp=(minimum_temperture<=current_temperature)& (current_temperature<=maximum_tempeture)
# # print("current temperture within minimum tempertur and maximum temp:",compare_temp)

# #if statement

# # temp_degree=float(input("enter the temperture"))
# # faren_temp=(temp_degree*(9/5))+32
# # print("temperature in the farenheit sacle is:",faren_temp)

# # if temp_degree<=15:
# #     print("temperature is not convicient ")
# # if temp_degree>=24 and temp_degree<= 28:
# #     print("temperature is convient for body")
     

# # base_salary=float(input("enter your base salary:"))
# # service_year=float(input("enter your service year:"))


# # if service_year<5:
# #     net_salary=(base_salary)-(0.12*base_salary)
# #     print("your net salalary is:",net_salary)
# # else:
# #     net_salary1=base_salary+0.12*base_salary-0.12*base_salary
# #     print("Your net salary is ", net_salary1)

# #USING LOOPS CONCEPT PRINT THE EVEN NUMBERS FORM 1 TO 50
# # i=1
# # while i<=50:
# #     if i%2==0:
# #         print(i)
# #     i=i+1


# # num=int(input("enter the number :"))
# # for i in range(1,11):
# #     print(num,"*",i,"=",num*i)\

# # items_num=int(input("enter the items your are purchased:"))
# # total_price=0
# # for i in range(items_num):
# #     price=float(input("enter the price of items your are purchased:"))
# #     total_price=( total_price+price)
# #     i=i+1
# # if total_price>=100:
# #             print("total price of items is:",total_price-total_price*0.1)

# # elif 50<=total_price<=99:
# #      print("your total price is :",total_price-total_price*0.05)
# # else:
# #      print("your not eligible for discount")
# #      print("your total prize is;", total_price)

# # for i in range(1,6):
# #     if i==3:
# #         continue
# #     print(i)
# # print("i am learning python")

# #electricity bill payment 
# # def electricity_bill():

# #     print("last date of electriciyt bill payment is next suday in pursing month")
# #     print("if you pay after dead line, your need to pay extra 100 rs of fine")
# #     print("hope you payment came before dead line, thank you!")
    
# # for i in range(3):
# #     name=input("enter your name:")

# #     unit=int(input("enter the units you have to be consumed:"))
# #     total_amount=unit*15
# #     print("the amount you have to pay",total_amount)
# #     electricity_bill()    


# def calculate_exam_score(exam_score):
#     total_leght=len(exam_score)
#     average_score=sum(exam_score)/total_leght
#     maximum_marks=max(exam_score)
#     minimum_marks=min(exam_score)

#     total_passed=0
#     for item in exam_score:
#         if item>=80:
#             total_passed=total_passed+1    

#         num_failed=total_leght-total_passed
#     return average_score,maximum_marks,minimum_marks,total_passed,num_failed
# exam_score=[10,50,40,80,90,100,400,50]
# average_score,maximum_marks,minimum_marks,total_passed,num_failed=calculate_exam_score(exam_score)
# print("average score is",average_score)
# print("maximu score is",maximum_marks)
# print("minimum score is",minimum_marks)
# print("total no students are passed:",total_passed)
# print("total no of student are failed:",num_failed)

# def grade_distribution(grade):
#     total_length=len(grade)
#     total_A_grades=0
#     total_B_grades=0
#     total_C_grades=0
#     total_D_grades=0
#     total_F_grades=0
    
#     for marks in grade:
#         if 90<=marks<=100:
#             total_A_grades=total_A_grades+1
           
#         elif 80<=marks<=89:
#             total_B_grades=total_B_grades+1
           
#         elif 80<=marks<=89:
#             total_C_grades=total_C_grades+1
           
#         elif 60<=marks<=69:
#             total_D_grades=total_D_grades+1
            
#         elif marks<=60:
#             total_F_grades=total_F_grades+1
           
#     failed_students=total_F_grades
#     return total_A_grades,total_B_grades,total_C_grades,total_D_grades,total_F_grades
# grade=[10,50,60,70,90,60,40,60,40,90,100,80]
# total_A_grades,total_B_grades,total_C_grades,total_D_grades,total_F_grades=grade_distribution(grade)
# print("A grade students",total_A_grades)
# print("B grades students", total_B_grades)
# print("C grades student",total_C_grades)
# print("D grades students are ",total_D_grades)
# print("F grade student",total_F_grades)

# def total_grades(grades):
#     for marks in grades:
#         if 90<=marks<=100:
#             print("Your got A grade")
#         elif 80<=marks<=89:
#             print("your got B grade")
#         elif 80<=marks<=89:
#             print("Your got  C grade")
#         else:
#             print("Your failed")
#     return
# grades=[10,82,40,100]
# total_grades(grades)
        

# import random

# def number_gussing_game(number):
#     gussing_mumber=0
#     while gussing_mumber<=8:
#         gussing_mumber=gussing_mumber+1
#         print("attemtps are",gussing_mumber)

        
#         user_no=int(input("enter the number:"))
#         if user_no==number:
#             print("congratulations You right guess!")
#             break
#         elif user_no>number:
#             print("Your guess number is greater the computer no")
#         elif user_no<number:
#             print("your guess number less than computer number")
#         else:
#             print('invalid number')
#     return
# number=random.randint(1,100)


# number_gussing_game(number)

                    
# def sum_of_sqaure(n):
#     total=0
#     for i in range(1,n+1):
#         square=i**2
#         print("square of number is:",square)
#         total=total+square
#     print("sum of total square n numbers is:", total)
# num=int(input("enter the number"))
# sum_of_sqaure(num)

# a="hello"
# b="world"
# d=a +" "+ b 
# print(d)#concatination
# c=len(a +" "+ b)#finding lenght of string
# print(c)
# sliceing=d[:6]
# print(sliceing)
# rev=d[-1:-12:-1]
# print(rev)
# up=rev.upper()
# print(up)
# print(up.replace("L","x"))
size_1=int(input("enter the size1 of the house:"))
bed_rooms1=int(input("enter the bed rooms1 you want:"))
price1=float(input("enter your buget1:"))
print()
size_2=int(input("enter the size2 of the house: "))
bed_rooms2=int(input("enter the bed rooms2 you wnat:"))
price2=float(input("enter your buget:"))

price_house_1=size_1*5000
price_house_2=size_2*5000

threshold_price=7500000
your_prize1=price_house_1>=threshold_price
your_prize2=price_house_2>=threshold_price
print("user1 price is grater than thresold price :", your_prize1)
print("user2 price is greater than the thresold price :",your_prize2)

























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































