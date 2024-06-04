'''One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the 
 ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. 
 They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.
Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way 
 that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts 
 are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should
 elp them and find out, if they can divide the watermelon in the way they want. For sure, each of them should 
get a part of positive weight.'''


w = int(input("weight of watermelon: "))
if(w%2!=0 or w<=2):
    print("No")
else:
    h=w/2
    if(h%2==0):
        print("weight of tw0 pieces are:",int(h),int(h))
    else:
        print("weight of two pieces are:",int(h-1),int(h+1))