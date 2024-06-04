#to remove an element from the tuple.
t = tuple(input().split(','))
l=len(t)
print(l)
i=int(input())
t=t[:i]+ t[i+1:]
print(t)

#alternate method
t=tuple(map(int,input().split()))
n=int(input())
#to convert tuple to the list
a=list(t)
a.remove(a[n])
#to convert list to tuple
b= tuple(a)
print(b)