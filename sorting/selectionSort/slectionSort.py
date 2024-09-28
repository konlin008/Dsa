arr=[45,12,3,65,4,12,34]
n=len(arr)
def selectionSort(array,n):
    for i in range(n):
        min=i
        for j in range(i,n):
            if array[j] < array[min]: min=j
        temp=array[min]
        array[min]=array[i]
        array[i]=temp
    return array
sortedArray=selectionSort(arr,n)
print(sortedArray)