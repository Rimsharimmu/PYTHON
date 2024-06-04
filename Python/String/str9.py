#to find the maximum occuring character in a given string

s=input()
max_char=max(s, key=s.count)
print(f"max occuring character: {max_char}")