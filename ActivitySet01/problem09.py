# Lists

filename = "ActivitySet01/romeo.txt"
#filename = input('Enter file name: ')
#fh = open("dataset/romeo.txt")
#lst = list()
#for line in fh:
    #words = line.split()
    #for word in words:
        #if word not in lst:
            #lst.append(word)
            #lst.sort()
#print(lst) 
filename=input('enter file name')
fhand = open('ActivitySet01/romeo.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = []
for key, val in counts.items():
	newtup = (val, key) 
lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)
