#we are finding calculated by empolyee net salary
print("-----------Enter the basic salary of empolyee-------------")
basic_salary=int(input("enter the basic salary of empolyee: "))
#if empolyee working in the professional company, company give TA, HRA
#we are finding hra and ta
HRA=basic_salary*0.10
TA=basic_salary*0.05
gross_salary=basic_salary+TA+HRA
print("the gross-salary of employee(without tax:", gross_salary)
#now Professional tax
p_tax=gross_salary*0.02
net_salary=(gross_salary-p_tax)
print("The net salary of the employee is:", net_salary)
print(vishal raut)