#fromkeys()
d={'a','b','c','d'}
d= dict.fromkeys(d,10)
print(d)

#setdefault() method
d={1:'hi','a':123, 100:32.4}
print(d.setdefault('a'))
print(d.setdefault('b'))
print(d)
print(d.setdefault('c',200))
print(d)