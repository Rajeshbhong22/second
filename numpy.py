# number=int(input("enter the number:"))
# result=0
# count=0
# while number !=0:
#     result+=number
#     count+=1
#     number=int(input("enter the number:"))

# print(result/count)

number=input("enter your number")

for i in range(len(number)-1,-1,-1):
    print(number[i], end="")


import keyword
print(keyword.kwlist)

    