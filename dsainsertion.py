a=[12,43,6,78,22]
n=len(a)
for i in range(1,n):
    index=i
    currnetval=a[i]
    for j in range(i-1,-1,-1):
        if a[j]>currnetval:
         a[j+1]=a[j]
         index=j
        else:
           break
        a[index]=currnetval
print(a)        