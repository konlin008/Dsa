def insertionSort(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while(j>0 and arr[j]< arr[j-1]):
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
        print(f"When i {i} arr is {arr}")
        
    print(f"sorted Array is &{arr}")
    
array=[14,9,15,12,6,8,13]
insertionSort(array)