#To store th inputs in the list
n= list(input().split(" "))
#mapping - a,b,c = map(datatype, sequence)
a,b,c = map(int,input().split(" "))
#Using map condition
n= list(map(int,input().split(" ")))
n.remove(n[1])
print(n)