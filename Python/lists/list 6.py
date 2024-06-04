a=list(map(int, input().split(" ")))
even =[]
odd = []
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort(reverse=True)
odd.sort()
l1=even+odd
print(l1)

'''a=list(map(int,input().split()))
b=[]
a.sort()
for i in a:
    if i%2==0:
        b.insert(0,i)
    else:
        b.append(i)
print(b)'''