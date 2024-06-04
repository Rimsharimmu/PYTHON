#to print th maximum count of a digit.
t = tuple(map(int,input().split(" ")))
c = 0
for i in t:
    if t.count(i)>c:
        c = t.count(i)
print(c)
print(i)

#alternative
my_tuple = (1, 2, 3, 2, 4, 2, 5, 2, 6)
max_count = max(my_tuple.count(item) for item in my_tuple)
print(f"Maximum count: {max_count}")