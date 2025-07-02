# set_math={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27}
# set_science={15,16,17,1,2,3,18,19,20,25,26,37,38,39,40,41,42,49,32,33,24,28,27}
# union_set=set_math.union(set_science)
# print("total number of student in math and science are:",union_set, len(union_set))
# #find total student inroll in both science and math 
# both_student=set_math.intersection(set_science)
# print("total number of student enroll in both math and science is:",both_student, len(both_student))
# #find number of student only enroll for math 
# only_math=set_math.difference(set_science)
# print("total number of student enrolled for math only",only_math, len(only_math))
# #find number of student enrolled onlu science is
# only_science=set_science.difference(set_math)
# print('total number of student enrolled only science is:',only_science, len(only_science))
# #find 


# # Write code here
# print("1.cm to ft\n2.km to miles\n3.USD to INR\n4.Exite")

# option=int(input("enter the number:"))
# if option==1:
#   length_cm=int(input("enter the value lenght in cm:"))
#   lenght_ft=length_cm/30.48
#   print("conversion is succesfull, Lenght in ft is :",lenght_ft)
# elif option==2:
#   distance_km=int(input("enter the distance in km:"))
#   distance_miles=distance_km*0.6213711
#   print("conversion is succesful distance in miles",distance_miles)
# elif option==3:
#   USD=int(input("enter the Money in USD:"))
#   INR=USD*80
#   print(f"conversion is sucesful{USD} USD= ",INR,"INR")
# else:
#   print("exite")

# Write code here
n=int(input("enter the number:"))
sum=0
while n>0:
  if n%5!=0:
    sum=sum+n
    if sum>=300:
      print(sum)
      break

