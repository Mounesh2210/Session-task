#using elif
#  0-35  d-grade
#     35-55-c-grade
#     56-70- b-grade  
#     70-100 A-grade  
#     invalid marks


m=int(input("Enter tamil mark: "))
if m>0 and m<=35:
    print("you are in Grade D")
elif m>35 and m<=55:
    print("you are in Grade C")
elif m>55 and m<=70:
    print("you are in Grade B")
elif m>70 and m<=100:
    print("you are in Grade A")
else:
    print("invalid marks")




#1. Greatest of Three Numbers

a=int(input("Enter value for a: "))
b=int(input("Enter value for b: "))
c=int(input("Enter value for c: "))

if a>b and a>c:
    print("Greatest of three number is",a)
elif b>a and b>c:
    print("Greatest of three number is",b)
else:
    print("Greatest of three number is",c)


#2. divisible by 3, 5, both, or neither.

n=int(input("Enter the number: "))
if n%3==0 or n%5==0:
    print("If number is divisible by 3 or 5: ",n)
else:
    print(" Neither divisible dy 3 and 5.")


#4.  Number to Day Converter   Description: Input a number (1 to 7) and print the corresponding day of the week (1 = Sunday, etc.).

d=int(input("Enter the day: "))
if d==1:
    print('Sunday')
elif d==2:
    print('Monday')
elif d==3:
    print('Tuesday')
elif d==4:
    print('Wednesday')
elif d==5:
    print('Thursday')
elif d==6:
    print('Friday')
else:
    print('Saturday')


#Validation & Conditions
#6..   Description: Simulate a basic login form by asking for a username and password, then validate them using if-else.


uname=input("Username: ")
passwd=int(input("Password: "))

if  uname=='mounesh' and passwd==1234 :
    print("Login Sucessfull...")
else:
    print("Login Unsucessfull...")


7. Voting Eligibility. Description: Ask for the users age and whether they have an ID. Check if they are eligible to vote using nested if conditions.

age=int(input('Enter your Age: '))
if age>=18 and age<100:
    print("YOu are eligible for vote.")