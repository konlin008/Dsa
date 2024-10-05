arr = [4, 2, 4, 3, 4, 1, 4]
low = 0
high = len(arr)-1

def pIndex(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<= pivot and i<=high -1:
            i +=1
            while arr[j]> pivot and j>=low +1:
                j -=1 
            if i<j:
                arr[i],arr[j] = arr[j], arr[i]
    arr[low],arr[j]= arr[j],arr[low] 
    return j        
    
def quickSort(arr,low,high):
    if low<high:
        parIndex= pIndex(arr,low,high)
        quickSort(arr,low,parIndex - 1)
        quickSort(arr,parIndex + 1,high)
        
quickSort(arr,low,high)
print(arr)