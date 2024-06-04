l = input().split()
#to sort the elements based on its length.
l.sort(key=len)
#to sort the elements in descending order.
l.sort(reverse=True)
#to swap the last and first elements.
l[0],l[-1] = l[-1],l[0]
'''temp = l[0]
l[0] = l[-1]
l[-1] = temp'''
print(l)