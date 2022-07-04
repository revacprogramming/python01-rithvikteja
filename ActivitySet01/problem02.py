  # Why Program
counts=dict()
print('the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car')
line=input('')
words=line.split()
print('Words:',words)
print('counting...')
for word in words:
  counts[word]=counts.get(word,0)+1
print('Counts',counts)  
  