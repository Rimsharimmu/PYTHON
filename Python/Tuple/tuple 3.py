# to remove an empty tuple(s) from a list of tuples.
list = [(),(),('',),(1,2),(1,2,3),(5)]
list = [t for t in list if t]
print(list)