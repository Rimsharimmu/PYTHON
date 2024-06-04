#to reverse a tuple.
t=tuple(map(int,input().split(" ")))
print(t[::-1])

#lternative method
x=tuple(input().split())
y = reversed(x)
print(tuple(y))