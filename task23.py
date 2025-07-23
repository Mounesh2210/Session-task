
'''55.	Create a program to sort elements in an array in ascending order.
56.	Write a program to find the length of the longest consecutive sequence in an array.
57.	Create a function to find the intersection of two arrays.
58.	Write a program to find the common elements between two arrays.
59.	Write a program to find the maximum consecutive ones in a binary array.
60.	Write a program to find the frequency of characters in a string.'''

'''#55'''
a=[12,45,12,28,64,53,87,64]
a.sort()
print(a)


'''#56'''
a=['apple','mango','pineapple','orange']

for i in a:
    # print(i)
    l=0
    s=0
    if len(i)>l:
        s=l
        l=len(i)
        # print(l)
    elif len(i)<l and len(i)>s:
        s=len(i)

print(l)

'''#57'''

def fun(a,b):
    list=[]
    for i in a:
        if i in b:
            list.append(i)
            
    return list

print(fun([1,2,3,4,5],[4,5,6,7,8,9]))

'''#58'''

a=['Apple','Mango','Orange']
b=['Pineapple','Apple','Graps']
c=[]
for i in a:
    if i in b:
        c.append(i)

print(c)

'''#59'''




'''$60'''

a={'hello everyone'}


for i in a:
    c=dict()

    for j in i:
        if j in c:
            c[j]+=1
        else:
            c[j]=1
    print(c)