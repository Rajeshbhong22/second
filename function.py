# heads=int(input("enter the total heads:"))
# legs=int(input("enter the total legs:"))
# goats=(legs-(2*heads))/2
# chickens=(4*heads-(legs))/2
# print("total number of goats are:",goats)
# print("total number of chickens are:", chickens)

# #creating tuple
# a=(1,2,3,4)
# print(a)
# print(type(a))

# #empty tuple
# tup=()
# print(tup)
# print(type(tup))
# #single element
# b=(5)
# print(b)
# print(type(b))
# b=(5,)
# print(b)
# print(type(b))
# #single element do not contain tuple

# #a tuple containing with mixed data types
# b=(1,23,"swati","nishant",True)
# print(b)
# print(type(b))

# #nested tuple
# a=(1,2.3,"mouse",(10,20,30))
# print(a)
# print(type(a))
# a=(1,2,3,"rajesh",[10,20,30])
# print(a)
# print(type(a))

# #tuple constructor
# empty=tuple()
# print(empty)
# print(type(empty))

# #converting list into a tuple
# list=[10,20,30,40,50,60,70,80]
# print(tuple(list),type(tuple(list)))

# #converting string into tuple

# String_example="hello"
# print(type(String_example))
# tuple1=tuple(String_example)
# print((tuple1))

# #conveting dictionary into tuple
# dict_example={"a":1,"b":2,"c":6}
# print(dict_example)
# print(type(dict_example))
# tuple1=tuple(dict_example)
# print(tuple1)

# #converting a set into a tuple
# set_example={1,2,3,4,5,6}
# print(set_example)
# print(type(set_example))
# tup=tuple(set_example)
# print(tup)
# print()
# print()

# #reversing the tuple
# t=(1,2,3,4,5,6,7,8)
# print(t[::])
# print(t[3:])
# print(t[:4])
# print(t[-1:2:-1])
# print()
# t=(1,2,3,4)
# del t


# product_dictonary={}
# for i in range(1,4):
#     id=int(input("enter the id of product:"))
#     name=input("enter the name of product:")
#     product_dictonary.update({id:name})
# print(product_dictonary)
l1=[1,2,3,4]
l2=[100,200,300,400]
list(zip(l1,l2))
