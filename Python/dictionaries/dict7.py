#To combine two dictionariy adding values for common keys.
from collections import Counter
d={}
d1 = {}
n = int(input())
for i in range(n):
    k=input()
    v=input()
    d[k]=v
    
for i in range(n):
    k=input()
    v=input()
    d1[k]=v

d2 = Counter(d) + Counter(d1)
print(d2) 