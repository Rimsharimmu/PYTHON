#to get the product of elements in the given range.
l=list(map(int,input().split(" ")))
a,b=map(int,input().split(" "))
product=1
for i in l:
    if i>=a and i<=b:
        product *=i
print(product)

'''
b=[]
for i in a:
    if i in range(m,n+1):
        b.append(i)
p=1
for i in b:
    p *= i
print(p)'''