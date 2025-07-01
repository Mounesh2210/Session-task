# find the given  number is even or odd
# find the find give number is leap year or not
# find the givn number is +ve or -ve
# gender-male age gretrthan 15 -> tickprice=100 or 50
# find the area of cirle 2pirsqr
#area of rectangle
#find the gold rate
#simple itnerst -pnr/100
# convert km into m
# convert cm into m
# bill and disc=30%  -> then your bill amount




#given  number is even or odd
num=int(input("Enter the Number: "))

if num%2==0:
     print("it is even number")
else :
    print("It is Odd number")


# find give number is leap year or not

year=int(input("Enter the year: "))

if year%4==0:
    print("Given year is leap year.")
else:
    print("Given year is Non-leap year.")


# find the givn number is +ve or -ve

n=int(input("Enter the Finding Number: "))

if n==0:
    Print("Input number is Zero.")

if n>0:
    print("It is Positive number.")
else :
    print("It is negative number.")

# gender-male age gretrthan 15 -> tickprice=100 or 50
name=input("Enter Your name:")
gen=input("Enter your Gender:")
age=int(input("Enter your age:"))

if gen=='male' and age<15 :
    print("Ticket price is ₹50")
else:
    print("Ticket price is ₹100.")


#find the area of cirle 2pirsqr
radius=int(input("Enter the radius of circle:"))
#2pi(r2)
#pi value 22/7

e=2*22/7*(radius**2)
print("Area of circle:",e)



#area of rectangle l*b

l=int(input("Enter the length of rectangle:"))
w=int(input("Enter the width of rectangle:"))


rect=l*w
print("Area of rectangle:",rect)


#find the gold rate
gold=int(input("Enter gram of gold:"))

g=gold*7440
print( "Total rate of gold is" ,g)



#simple itnerst = (P * R * T) / 100
amount=int(input("Enter SI amount:"))
rate=int(input("Enter rate of intrest:"))
time=int(input("Enter time in month:"))

si=(amount*rate*time/12)/100
print("Your Intrest is: ",si)


# convert km into m
km=int(input("Enter your km/h:"))

k=km*1000
print("Meter: ",k)



# convert cm into m
cm=int(input("Enter your cm:"))

c=cm*0.01
print("Meter: ",c)


# bill and disc=30%  -> then your bill amount
bill=int(input("Enter your bill amount: "))
dis=int(30)
tot=(bill/100)*dis
total=bill-tot
print("Total bill amount:",total)




