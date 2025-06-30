#systax:syntax is the grammer of writing code in programming language.\
print("rajesh")
print('rajesh')
print("""rajesh""")
print(12)
print(True)
print(False)
print("name", " age", "course")
print(12,23,45,4)
print("rajesh", 12,"python",True,False)
#complex datatype
print(3+5j)
print(type(3+5j))
print(type(4))
print(type(4.5))
print(type(True))
#list=it is an ordered sequence items.lsit is mutable, list iterable, it contain same or different data init.
#homogeneous list:it contain same datatype
a=[1,2,3,4,5,6,4,5,6]
print(list)
print(type(list))
#heterogeneous list:it contain different data type
print([10,20,30,"rajesh", "kashinath","bhong"])
#it is similar about set, tuple, dictionary

#in python type( function to check which type of data contain
#types of binding in python
#statuc typing= need to decalre datatype before usign declaring variable
#int a=20
#dynamic typing: no need to decalre datatype before assining value to the varible

import keyword
print(keyword.kwlist)



a=int(input("enter the number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a==b==c:
    print('given numbers are same')
elif a<b and a<c:
        print(f"number {a} is less than {b} and {c}")
elif b<a and b<c:
    print(f" number {b} is less than {a} and {c}")
else:
     print(f'number {c} is less than {a} and {b}')
          