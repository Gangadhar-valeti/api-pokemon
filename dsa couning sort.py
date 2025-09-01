def counting(array):
    maxval=max(array)
    count=[0]*(maxval+1)

    while len(array)>0:
      num=array.pop(0)
      count[num]+=1

    for i in range (len(count)):
       while count[i]>0:
          array.append(i)
          count[i]-=1

    return array

unsortedarray=[3,5,1,3,4,12,5,2,2,2]
sortedarray=counting(unsortedarray)     
print("sorted array=",sortedarray) 
