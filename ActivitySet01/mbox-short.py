#import re

#lin='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#y=re.findall('@([^ ]*)',lin)
#print(y)
#fhand=open('ActivitySet01/mbox-short.txt')
#numlist=list()
#for line in fhand:
  #line=line.rstrip()
  #stuff=re.findall('^X-DSPAM-CONFIDENCE: ([0-9])',line)
 # if len(stuff)!=1:continue
 # num=float(stuff[0])
 # numlist.append(num)
#print('Maximum:',max(numlist))  
#string="Python is fun"
#s=re.search('Python',string)
#print(s)
#fhand = open('ActivitySet01/mbox-short.txt')



#for line in fhand:
    #line = line.rstrip()
    #if not '@uct.ac.za' in line : 
     # continue
    #print(line)
import re

fhand = open('ActivitySet01/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)


     
 