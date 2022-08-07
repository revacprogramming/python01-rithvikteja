

s1={'apple','banana','cherry'}
print(s1)
S1 = {"apple", "banana", "cherry"}

for x in S1:
  print(x)
  S1 = {"apple", "banana", "cherry"}

print("banana" in S1)
S1 = {"apple", "banana", "cherry"}

S1.add("orange")

print(S1)
S1 = {"apple", "banana", "cherry"}

S1.update(["orange", "mango", "grapes"])

print(S1)
S1 = {"apple", "banana", "cherry"}

print(len(S1))
S1 = {"apple", "banana", "cherry"}

S1.remove("banana")
print(S1)
S1 = {"apple", "banana", "cherry"}

S1.discard("banana")

print(S1)
S1 = {"apple", "banana", "cherry"}

x = S1.pop()

print(x)

print(S1)
S1 = {"apple", "banana", "cherry"}

S1.clear()

print(S1)

S1 = {"apple", "banana", "cherry"}

del ()
print(S1)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
D1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(D1)
for x in D1:
  print(x)
  D1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in D1:
  print("Yes, 'model' is one of the keys in the d1 dictionary")
  D1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
D1.pop("model")
print(D1)
D1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
D1.popitem()
print(D1)

D1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del D1["model"]
print(D1)
D1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
D2 = D1.copy()
print(D2)







