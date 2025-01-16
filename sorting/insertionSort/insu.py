def insu(arr):
    n= len(arr)
    swaps 
    for i in range (n):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
        print(arr)
        
        
arr=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
insu(arr)