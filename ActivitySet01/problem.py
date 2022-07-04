l1=['a','b','c','d','e']
s1={'a','b','c','d','e'}
print(l1)
print(s1)
print(type(l1))
print(type(s1))
a_list=['a','b','mpilgrim',True,False,42]
a_set=set(a_list)
s=[]
s=print(set(range(1,6)))
a_set={1,2}
a_set.add('reva')
print(a_set())
a_set={1,2}
a_set.update({2,4,6})
print(a_set)
s1={1,2,3,4,5}

>>> for i in s1:
...   print(i)
... 
1
2
3
4
>>> 3 in s1
True
>>> 0 in s1
False
>>> s1={1,2}
>>> s2=s1
>>> s2
{1, 2}
>>> s1
{1, 2}
>>> s2.pop()
1
>>> s2
{2}
>>> s1
{2}
>>> s1={1,2}
>>> s2=s1.copy()
>>> s2
{1, 2}
>>> s1
{1, 2}
>>> s2.remove(2)
>>> s2
{1}
>>> s1
{1, 2}
>>> s1={1,2}
>>> s2={2,3}
>>> s1.union(s2)
{1, 2, 3}
>>> s1={1,2}
>>> s2={2,3}
>>> s1|s2
{1, 2, 3}
>>> s1.intersection(s2)
{2}
 s1={1,2}
>>> s2={2,3}
>>> s1 and s2
{2, 3}
>>> s1.difference(s2)
{1}
s1={1,2}
>>> s2={2,3}
>>> s1.symmetricdifference(s2)
>>> s1^s2
{1, 3}
s1.isdisjoint(s2)
False
 s1.isdisjoint({5,4})#if it is different it is true
True

>>> {1,2}.issubset({2,3})#it should have all elements of subset
False
>>> {1,2}.issubset({1,2,3})
True
 {1,2}.issuperset({2,3})
False
{1,2,3}.issuperset({2,3})
True
