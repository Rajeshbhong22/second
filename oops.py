# #constructor
# class Student:
#     def __init__(self):
#         self.name=input("enter your name:")
#         self.rollno=int(input("enter your roll no:"))
#         self.course=input("enter your course:")
#     def display(self):
#         return(self.name, self.rollno, self.course)
# a1=Student()
# a1.display()

# #paraameterized constructor
# class Addition:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         self.c=self.a + self.b
#     def display(self):
#         return(self.c)
# a1= Addition(11,22)jhdsjh
# a1.display()

#wap program accept person name, age , through the parameterized function

# class Student:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def check_file(self):
#         if self.age<18:
#             return("your not eiligible for voting")
#         else:
#             return("your eligible for voting")
# a1=Student("rajesh",15)
# a1.check_file()

#magic methods
#__init__(): it is a constructor
#__str__(): used to return

# class student:
#     def __init__(self):
#         self.name=input("enter the your name:")
#         self.rollno=int(input('enter the roll no:'))
#     def __str__(self):
#         return f'{self.name , self.rollno}'
# s1=student()
# return(s1)

# class Demo:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         self.a+=self.b
#         return("addition:", self.a)
#     def multiplication(self):
#         self.a*+self.b
#         return("multiplication:", self.a)
#     def sub(self):
#         self.a-=self.b
#         return(self.a)
#     def division(self):
#         self.a/=self.b
#         return(self.a)
# s1= Demo(11,22)
# s1.add()

# class Demo:
#     def __init__(self, a,b):
#         self.a=a
#         self.b=b
#     def __add__(self, other):
#         self.a+=other.a
#         self.b+=other.b
#         return(self.a, self.b)
#     def __sub__(self,other ):
#         self.a-=other.a
#         self.b-=other.b
#         return(self.a, self.b)
#     def __mul__(self,other):
#         self.a*=other.a
#         self.b*= other.b
#         return (self.a, self.b)
#     def __truediv__(self, other):
#         self.a/=other.a
#         self.b/=other.b
#         return (self.a, self.b)
# s1=Demo(11,22)
# s2=Demo(11,22)
# print(s1+s2)


# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
#     def __eq__(self, other):
#         return self.marks==other.marks
#       def __ne__(self, other):
#           return self.marks == other.marks
#       def __gt__(self, other):
#           return self.marks == other.marks
#       def __ge__(self, other):
#           return self.marks == self.marks
#       def __lt__(self, marks):
#           return self.marks 
# a1=Student("rajesh",11)
# a2=Student("sushant",12)
# print(a1==a2)


#passing reference: passing object as parameter
class mango:
    def __init__(self, color, teaste, type):
        self.color=color
        self.teaste=teaste
        self.type=type
    def display(s1):
        print("colour:",s1.color,"teaste:",s1.teaste,"type:",s1.type)


s1=mango("reddish","sweet","ratnagiri")
s1.display()

