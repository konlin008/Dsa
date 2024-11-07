# nums = [1,2,3,4,5,6,7] 
# n= len(nums)
# k = 3
# def leftRoate(arr,n,k):
#     temp= arr[:k]
#     for i in range(k,n):
#         arr[i-k]= arr[i]
#     for j in range(n-k,n):
#         arr[j]=temp[j-(n-k)]
#     print(arr)
# leftRoate(nums,n,k)   





nums = [-1,-100,3,99] 
n= len(nums)
k = 2

def leftRoate(nums,n,k):
    def reverse(arr,start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start +=1
            end -=1
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    print(nums)        
leftRoate(nums,n,k)    