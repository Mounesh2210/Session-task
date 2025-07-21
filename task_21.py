'''47.	Write a function to find the length of the last word in a string.
48.	Write a program to find the largest prime factor of a given number.
49.	Implement a program to calculate the square root of a number.
50.	Write a program to find the sum of digits of a given number until it becomes a single digit.
51.	Implement a program to find the sum of all even numbers in an array.
'''

#1
def strr(a):
    s=a.split()
    for i in s:
        count=0
    print(i)
    for j in i:
        count+=1
    print('Length of the last word:',count)
    return count


strr('apple mango orange')
# print(strr('apple mango orange'))

# 2
a=12
is_prime=True
fact=[]
pri=[]
for i in range(1,a+1):
    if a%i==0:
        fact.append(i)
print(fact)
for l in fact:
    is_prime=True
    for j in range(2,l):
        if l%j==0:
            is_prime=False
    if is_prime:
        pri.append(l)
print(pri)

for k in range(len(pri)):
    l=0
    s=0
    d=pri[k]
    # print(pri[k])
    if d>0:
        s=0
        l=d
    elif d<l and d>s:
        s=d
print('largest fact of 0:',l)




#3
import math

a=12
print(f'square root of {a} is {math.sqrt(a)}')


#4
i=1
s=0
for i in range(1,5):
    print(i)
    while(s<10):
    # print(i)
        s+=i
print(s)


#5
def sum(num):
    a=0
    for i in range(len(num)):
        if i%2==0:
            a+=num[i]

    return f'Sum of even number is {a}'

print(sum([1,2,3,4,84,64,24,51]))
