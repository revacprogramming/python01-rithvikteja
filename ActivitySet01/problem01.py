#r="ActivitySet01/problem01.txt"
#a= open(r,"r")
#print(a)
#c=0
#a=open('ActivitySet01/problem01.txt')
#count=0
#for line in a:
 # count=count+1
#print("linecount:",count) 

 
 
#for line in a:
 # if not line.startswith('X-Content'):
    #print(line)
    #c=c+1
#print(c)    

#fh=open("ActivitySet01/problem01.txt")

#for line in fh:
 # liney=line.rstrip()
  #print(liney.upper())
counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
  counts[name]=counts.get(name,0)+1
print(counts)  
  
