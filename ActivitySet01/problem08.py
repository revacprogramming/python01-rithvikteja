# Files

filename = "dataset/mbox-short.txt"
fname = input("enter file name: ")
#fh = open("dataset/mbox-short.txt")
#count = 0
#average = 0
#for line in fh:
    #if not line.startswith("X-DSPAM-Confidence:") : continue
    #average += float(line[20:-1].strip())
    #count = count + 1
    #print(line)
    
#print("Average spam confidence:", (average/count))
import re
fhand=open('mbox-short.txt')
for line in fhand:
  line=line.rstrip()
  if re.search('From:',line):
    print(line)