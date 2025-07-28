'''1. Student Score Analysis
Description:Given an array of student objects like this:
const students = [
  { name: "Akash", marks: 87 },
  { name: "Meena", marks: 92 },
  { name: "Rahul", marks: 76 },
  { name: "Priya", marks: 95 },
  { name: "Vikram", marks: 63 },
  { name: "Sneha", marks: 89 },
  { name: "Karan", marks: 54 },
  { name: "Divya", marks: 99 },
  { name: "Sanjay", marks: 81 },
  { name: "Anita", marks: 70 }
];
Task Requirements:
Filter students who scored above 90.
Convert names to uppercase using map().
Sort by marks descending.
Calculate average marks using reduce().'''


students = [
  { 'name': "Akash", 'marks': 87 },
  { 'name': "Meena", 'marks': 92 },
  { 'name': "Rahul", 'marks': 76 },
  { 'name': "Priya",'marks': 95 },
  { 'name': "Vikram", 'marks': 63 },
  { 'name': "Sneha", 'marks': 89 },
  { 'name': "Karan", 'marks': 54 },
  { 'name': "Divya", 'marks': 99 },
  { 'name': "Sanjay",'marks': 81 },
  { 'name': "Anita", 'marks': 70 }
]


# m=[i for i in students if i['marks']>90]
# print(m)


# ma=list(map(lambda x:x['name'].upper(),(students)))
# print(ma)

# students.sort(key=lambda x: x['marks'], reverse=True)
# print(students)




'''2. Email Verifier and Formatter
Description:
Given an array of email IDs:

const emailList = [
  "john.doe@gmail.com",
  "JANE.SMITH@yahoo.com",
  "  alice@outlook.com ",
  "bob_the_builder@protonmail.com",
  "charlie123GMAIL.COM",
  "emma.watson@gmail.com",
  "test.user@YAHOO.COM ",
  "mike@icloudcom",
  " nina99@zoho.com",
  "user@example.com "
];

Task Requirements:

Trim whitespaces and convert all emails to lowercase.

Validate whether each email contains @ and ends with .com.

Count how many are valid.'''

email = [
  "john.doe@gmail.com",
  "JANE.SMITH@yahoo.com",
  "  alice@outlook.com ",
  "bob_the_builder@protonmail.com",
  "charlie123GMAIL.COM",
  "emma.watson@gmail.com",
  "test.user@YAHOO.COM ",
  "mike@icloudcom",
  " nina99@zoho.com",
  "user@example.com "
]
import re
cl=[]
for i in email:
   cl.append( i.strip().lower())
print(cl)


print('<-=---------------------------------------------------------------->')
# for i in email:
for i in cl:
    # print(i)
    patt=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    e=re.match(patt,i)
    if e:
      print(i) 

print('<----------------------------------------------------------->')
count=0
# for i in email:
for i in cl:
    # print(i)
    patt=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    e=re.match(patt,i)
    if e:
      count+=1

print(count)

'''3. Upcoming Events Scheduler
Description:
You are given an array of event dates (as strings).

const dateList = [
  "2025-07-25",
  "2024-12-10",
  "2025-01-01",
  "2023-05-14",
  "2026-08-09",
  "2022-11-30",
  "2025-04-18",
  "2024-09-21",
  "2025-12-25",
  "2023-01-10",
  "2026-03-17",
  "2024-02-29",
  "2025-10-05",
  "2023-07-01",
  "2025-06-15",
  "2024-04-01",
  "2025-11-11",
  "2022-12-31",
  "2024-06-30",
  "2025-09-09"
]

Task Requirements:
Convert them into Date objects.
Filter only future events.
Sort them in ascending order.
Format each date as DD-MM-YYYY.'''


from datetime import datetime
dateList = [
  "2025-07-25","2024-12-10","2025-01-01","2023-05-14","2026-08-09",
  "2022-11-30","2025-04-18","2024-09-21","2025-12-25","2023-01-10",
  "2026-03-17","2024-02-29","2025-10-05","2023-07-01","2025-06-15",
  "2024-04-01","2025-11-11","2022-12-31","2024-06-30","2025-09-09"
]

# for i in dateList:
#     a=datetime.strptime(i,"%Y-%m-%d")
#     print(a)


print('<---------------------------------------------------------------------->')

# today = datetime.now().date()
# for i in dateList:
#     d=datetime.strptime(i, "%Y-%m-%d").date()
#     # print(d)
#     if d > today:
#         print(d)
            

print('<---------------------------------------------------------------------->')

# sort= sorted([i for i in dateList] )
# s=[i for i in sort]
# print(s)


print('<---------------------------------------------------------------------->')
# for i in dateList:
#   da=datetime.strptime(i,"%Y-%m-%d")
#   date=da.strftime('%d-%m-%Y')
#   print(date)
