# Network Programming
# https://www.py4e.com/essons/network
a=str(input('enter a string'))
def reverse(a):
  b=""
  for i in a:
   b=i+b
  return b
b=reverse(a)
if a==b:
  print('palindrome')
else:
  print('not palindrome')