#to check whether a given key already exists in a dictionary.
import operator
d = {}
n = int(input())
for i in range(n):
    k = input()
    v = input()
    d[k] = v
key=input()
if key in d:
    print('key is present in the dictionary')
else:
    print('key is not present in the dictionary')