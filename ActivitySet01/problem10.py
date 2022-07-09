# Dictionaries

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    filename = "database/mbox-short.txt"
fh= open(filename)
counts = dict()

for line in fh:
    if line.startswith('From ') :
        words = line.split()
        time = words[5]
        hours = time[:2]
        counts[hours] = counts.get(hours,0) + 1

for key, val in sorted(counts.items()):
    print (key, val)