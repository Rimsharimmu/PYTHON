a=list(map(int,input().split(" ")))
#or a=input().split(" ")
b=list(map(int,input().split(" ")))
#or b=input().split(" ")
c=a+b
c.sort()
c=[int(i) for i in c]
print(c)