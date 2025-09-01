def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return i+1      
def quicksort(array,low=0,high=None):
    if high is None:
        high=len(array)-1
    if low<high:
        pivotinex=partition(array,low,high)
        quicksort(array,low,pivotinex-1) 
        quicksort(array,pivotinex+1,high)
my_array=[53,6,5,3,55,4342,5938]    
quicksort(my_array) 
print(f"quick sorted arraay{my_array}")   
            
