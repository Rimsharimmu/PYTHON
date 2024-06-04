#python program to remove a key from a dictionary
d = {}
n = int(input())
for i in range(n):
    k,v = map(int,input().split(" "))
    d[k]=v
    
a = int(input())
d.pop(a)
print(d)

#or
'''if key in d:
    del d[key]
print(d)'''