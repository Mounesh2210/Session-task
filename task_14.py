# 1..GST Calculation for Hotel Bill 


# room=int(input("How many days: "))
# rate=4000
# tot=0
# total=0
# bill=(room*rate)
# print(bill)

# if rate>0 and rate<=1000:  
#     total=room*rate
# elif rate>1000 or rate<=7500:
#     tot=(rate*room/100)*12
#     total=bill+tot
# else:
#     tot=(rate*room/100)*18
#     total=tot+bill

# print('Room per night is ₹4000')
# print(f"Total amount :{total}")


#2️ Fibonacci Series 

# n=int(input('Enter the number:'))
# a=0
# b=1
# list=[]
# for i in range(n):
#     if a<=b:
#         list.append(a)
#         a=a+b
#     else:
#         list.append(b)
#         b=a+b
# print(list)

# 3️Grading System 


# mark=int(input("Enter your Mark: "))

# if mark>=90 and mark<=100:
#     print('Grade A')
# elif mark>=80 and mark<=89:
#     print('Grade B')
# elif mark>=70 and mark<=79:
#     print('Grade C')
# elif mark>=60 and mark<=69:
#     print('Grade D')
# else:
#     print('Faile')

# 4️Factor Finder 

# for i in range(1,20+1):
#     print(i)
#     fact=[]

#     for j in range(1,i):
#         if i%j==0:
#             fact.append(j)
#     print(fact)

#5️Leap Year Checker 

# for i in range(2000,2050+1):
#     if i%4==0 :
#         print("Leep Year.")
#     else:
#         print(i)


#6️.Simple Interest Calculator 

# p=int(input("Enter the principal amount: "))
# r=int(input("Enter rate of intrest:  "))
# t=int(input ("Enter time:  "))
# si=0

# si=(p*r*t)/100

# print("Simple Intrect:",si)


# 7️.Surface Area of a Cylinder 

# r=int(input("Enter the radies: "))
# h=int(input ("Enter the height: "))
# p=2*22/7
# tsa=(p*(r*h))+(p*(r**2))

# print("Total surface Area is ",tsa)


#8️.Temperature Converter 

# c=int(input("Enter the Celsius.: "))

# f=9/5*c+32

# print("Fahrenheit is ",f)

# 9️.Discount Calculation 

amount=50000
dis=5

print("Total bill amount is ",amount*dis/100)

#10 Electricity Bill Calculator
name=(input("Enter the name: ")) 
u=int(input("Enter the unit: "))
amt=0
if u<0 and u>=100:
    amt=u*3
elif u<101 and u>=200:
    amt=u*5
elif u<201 and u>=300:
    amt=u*7
else:
    amt=u*10
print(f'{name} used {u} units a month bill was {amt}')