nums = [1,2,3,4,5,6,7] 
n= len(nums)
k = 3
def leftRoate(arr,n,k):
    temp= arr[:k]
    for i in range(k,n):
        arr[i-k]= arr[i]
    for j in range(n-k,n):
        arr[j]=temp[j-(n-k)]
    print(arr)
leftRoate(nums,n,k)   
