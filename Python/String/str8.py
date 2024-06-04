#to create a string from 2 given strings concatenating uncommon characters of the said strings
''' Hello
World            -------> HeWrd'''

s1=input()
s2=input()
s=''
s3=s1+s2
for i in s3:
    if s3.count(i)==1:
        s += i
print(s) 