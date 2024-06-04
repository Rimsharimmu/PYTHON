#to move all the spaces to the front of a given string in single traversal

#python program--> pythonprogram

s=input()
spaces=""
result=""

for char in s:
    if char==" ":
        spaces += char
    else:
        result += char

final_str= spaces+result
print(final_str)

str=input()
count =0
for i in str:
    if(str[1]==' '):
        count +=1

print(str)   
