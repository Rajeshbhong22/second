'''#write a program to print number from 10 to 15.
a=10
while a<=15:
    print(a)
    a+=1

#print  cube og numbers using while loop 1 to 5
a=1
while a<=5:
    print(a**3, end=" ")
    a+=1


#prit odd unbers from one to 10
a=1
while a<=10:
    if a%2!=0:
        print(a, end="")
    a+=1
print()

#calculate the product of number 1 to 5
product=1
number=1
while number<=5:
    product*=number
    number+=1
print(product)
#question no 5

string=input('enter the stirng:')
words=string.split()
for word in words:
    i=len(word)-1
    while i>=0:
        print(word[i], end="")
        i-=1
    print(" ", end=" ")
    print()

#lefht not using
string=input('enter the string:')
count=0
index=0
while index<len(string):
    count+=1
    index+=1
print(count)

multiple=4
count=1
while count<=10:
    print(multiple, end="")
    multiple+=4
    count+=1'''


    
    

print("hellow world")

