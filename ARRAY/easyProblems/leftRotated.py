arr = [1,2,3,4,5,6,7]

def leftRotatedArray(arr):
    temp= arr[0] 
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]= temp
    print(arr)
    
leftRotatedArray(arr)