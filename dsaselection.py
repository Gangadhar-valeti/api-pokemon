a=[3,7,1,9,13]
n=len(a)
for i in range(n):
    minval=i
    for j in range(n-1):
        if a[j]>a[minval]:
            minval=j
        a[i],a[minval]=a[minval],a[i]
print(a)              

