l= list(map(int,input().split(" ")))
a=[]
for i in range(len(l)):
    if i not in a:
        a.append(l[i])
a.sort()
#to get sum of maximum numbers in the list we use
#a.sort(reverse = True)
sum= a[0] + a[1] + a[2]
print(sum)

'''a=list(map(int,input().split()))
a.sort()
print(sum(a[:3]))'''