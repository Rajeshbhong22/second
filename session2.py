# #arthematic opertors
# print(5+6)#additon
# print(5-6)#substraction
# print(5*6)#multiplication
# print(5/2)#division
# print(5//2)#floor division
# print(5%2)#modulus
# print(5**2)

# #bit wise operator

# print(4 & 5)

# #bitwise or
# print(4 | 5)
# #bitwise xor
# print(9 ^ 5)

# print(~5)
# #bit wise right shift 
# print(4>>2)
# print(8>>2)
# #bitwise left shift
# print(4<<2)
# print(9<<2)

# print("hello world")

# # class raj:
# #   def accept(self):#self represent the current object
# #     self.rollno=int(input("enter the roll nO.: "))
# #     self.name=input("enter the name:")
# #     self.marks=int(input("enter the marks:"))
# #   def display(self):
# #     print(self.rollno, self.name, self.marks)
# # s1= raj()
# # s1.accept
# # s1.display()

# # s2= raj()
# # s2.accept()
# # s2.display()

# # class rajesh:
# #   def biodata(self): #self represent the current object
# #       self.coll =input("enter your college:")
# #       self.course =input("enter your course name:")
# #       self.fees =int(input('enter your college fees:'))
# #       self.sgpa =float(input("enter your course sgpa:"))
# #   def display(self):
# #     print( "college", self.coll)
# #     print("course", self.course)
# #     print("fees",self.fees)
# #     print("sgpa", self.sgpa)

# # s1=rajesh()
# # s1.biodata()
# # s1.display()


# # class Student:
# #     def __init__(self):
# #         self.college=input('enter your college:')
# #         self.course=input("enter your course:")
# #         self.sgpa=int(input("enter your sgpa:"))
# #         self.fees =int(input("enter the college fees:"))
# #     def display(self):
# #         print(self.college, self.sgpa , self.course, self.fees)
# # s1=Student()
# # s1.display()


# class calculation:
#     def __init__(self, a,b):
#         self.a=a
#         self.b=b

#     def add(self):
#         self.a+=self.b
#         print(self.a)
# s1=calculation(11,22)
# s1.add()



# #magic method or dunnder method
# '''1. __init__ ; constructor
# 2. __str__; string representation
# '''
# class car:
#     def __init__(self, color, model):
#         self.color=color
#         self.model=model
#     def __str__(self):
#         return f'my car {self.color} and model is {self. model}'
# s1=car('red','tata')
# print(s1)
# #using constructor only

class Employee:
  def __init__(self, name ,salary):
    self.__name= name
    self.__salary= salary
  def set_name(self, new_name):
    if new_name.isalpha():
      print(self.__name==new_name)
    else:
      print(self.__name)
  def set_salary(self, new_salary):
      if new_salary>25000:
        print("enter salary", self.__salary)
      else:
        pass
e1=Employee("enter string formate", "salary must be 25k")
e1.set_name("rajesh")
e1.set_salary(26000)