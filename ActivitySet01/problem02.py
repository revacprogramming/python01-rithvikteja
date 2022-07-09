

txt = 'but soft what light in yonder window breaks'
words = txt.split()

t = list()
for word in words:
    t.append((len(word), word))#add items to the previous list


t.sort(reverse=True)
 

res = list()
for length, word in t:
   res.append(word)
print(res)


t1=('apple','banana','cherry')
print(t1)



