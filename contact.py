# # familiy={ 
# #     'rajesh bhong':{'age':18, 'contact':8329277264, "occupation":"engineering student" },
# #     'kashinath bhong':{ 'age': 37, 'contact': 8975462585, "occupation": 'electronics engineer'},
# #     'shubhangi bhong':{ 'age':16,"contact": 7219503561, "occupation": "student"},
# #     'shashikala bhong': {"age":36,'contact': 9730630128, "occupation": "House wife"     }

# # }
# # print(familiy)
# # print(familiy['kashinath bhong']['age'])
# # for a,b in familiy.items():
# #     print(a,b['contact'])


# #tuples in python
# #creating tuple
# t=(10,20,30,40)
# print(t, type(t))
# #empty tuple
# t=()
# print(t, type(t))
# #single tuple
# t=(10)
# print(t)
# print(type(t))
# t=(10,)
# print(t) 
# print(type(t))
# #tuple with mixed data types
# t=(10,20,30,40)*5
# print(t)
# t=("name",10,20,True,False)
# print(t)
# #nested tuple
# t=(10,20,30,40,50,60,(30,40,50))
# print(t)
# print(type(t))

# print()
# #tuple constructor
# t=tuple()
# print(t, type(t))
# #converting list into tuple
# tup=(1,2,3,4,5,6,7,8,9)
# lt=list(tup)
# print(lt)
# print()
# list=[10,20,30,40,50,60,70]
# tuple=tuple(list)
# print(tuple)
# # print()
# # #converting string into tuple
# # dictonary={"a":1, "b":2,"c":3}
# # tup=tuple(dictonary.items())


# class Student:
#   def __init__(self):  # self represents the current object
#     self.rollno = int(input("Enter the roll no.: "))
#     self.name = input("Enter the name: ")
#     self.marks = int(input("Enter the marks: "))

#   def display(self):
#     print("Roll No.:", self.rollno)
#     print("Name:", self.name)
#     print("Marks:", self.marks)

# # create a student object
# s1 = Student()

# # call display() method using the object
# s1.display


class Student:
    def __init__(self,name,salary):
        self.salary=salary
        self.name=name
    def get_name(self):
        return self.name
    def set_name(self, name):
        if name.isalpah():
            self.name=name
            return self.name
        else:
            print("name enter in a string")
    def get_salary(self):
        return self.salary
    def set_salary(self, salary):
        if salary>25000:
            self.salary=salary
            print("enter salary below,25k")
        else:
            print(self.salary)
a1=Student("rajesh",25000)
a1.get_name("mahesg")
a1.get_salary(25000)      
                 

        