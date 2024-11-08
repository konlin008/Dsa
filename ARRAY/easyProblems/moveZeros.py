nums = [0]
def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i]==0:
            j=i
            break
    for i in range(j+1,len(nums)):
        if nums[i] !=0:
            nums[j],nums[i]=nums[i],nums[j]
            j +=1
            print(nums)
moveZeroes(nums)    