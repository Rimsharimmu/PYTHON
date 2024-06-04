n=int(input())
a=[input().split()for i in range(n)]
for i in range(0,n):
    for j in range(0,n-i-1):
        a[j],a[j+1]