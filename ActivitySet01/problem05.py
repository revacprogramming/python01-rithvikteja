# Functions


def computepay(h, r):
    
  if h>40:
    p=r*40+(h-40)*1.5*r
  else:
   p=h*r
  return p
  

hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
