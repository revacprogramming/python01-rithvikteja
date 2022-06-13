# Regular Expressions
# https://www.py4e.com/lessons/regex
num=int(input("enter the range number:"))
first_value=0
second_value=1
for n in range(0,num):
 if(n<0):
   next=n
 else: 
   next=first_value+second_value
   first_value=second_value
   second_value=next
print(next)   