#brut
def misssingNumber(arr):
    for i in range(len(arr)+1):
        flag=0
        for j in range(len(arr)):
            if arr[j]==i:
                flag=1
                break
        if flag==0:
            print(i)
nums = [0,1] 
misssingNumber(nums)


#better solution 
n=len(nums)
def misNum(nums,n):
    
    hash_Arr=[0]*(n+1)
    
    for i in range(n):
        hash_Arr[nums[i]]=1
        
    for i in range(n+1):
        if hash_Arr[i]==0:
            print(i)
misNum(nums,n)

#optimal

def missingNum(nums,n):
    sum1=n*(n+1)//2
    sum2=0
    for i in range(n):
        sum2 +=nums[i]
    print(sum1-sum2)
missingNum(nums,n)