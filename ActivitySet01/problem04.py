# Conditional Execution

sh=input("Enter hours: ")
sr=input("enter rate: ")
fh=float(sh)
fr=float(sr)
if fh<=40:
  print(fh * fr)
elif fh>40:
  print(fr*40+(fh-40)*1.5*fr)