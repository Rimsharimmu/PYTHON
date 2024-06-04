#python program to map two lists into dictionary.
a= list(map(int,input().split(" ")))
b= list(map(int,input().split(" ")))
d={ a[i]:b[i] for i in range(len(a)) }
print(d)

#alternative:

keys=input().split()
values=input().split()
d=dict(zip(keys, values))
print(d)

#or
l1=[1,2,3]
l2=[5,6,7]
for i in range(0,3):
    key=l1[i]
    value=l2[i]
    d[key] = value
print(d)