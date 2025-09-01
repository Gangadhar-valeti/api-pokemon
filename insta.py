a=[2,7,12,15]
target=9
for i in range(len(a)):
    for j in range(i):
        if a[i]+a[j]==target:
            print(a[i],a[j])


b=[1,3,5,1,5]
for num in range (len(b)):
    if b.count(num)==1:
     print(num)   

c=[1,3,3,1,4]
result=0
for nums in c:
   result ^=nums
print(result)                