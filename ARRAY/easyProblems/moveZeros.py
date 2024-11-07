nums = [0,1,0,3,12]
def moveZeroes(nums):
    n=len(nums)
    i=nums[0]
    for j in range(0,n):
        if nums[j] != 0:
            nums[i],nums[j]=nums[j],nums[i]
            i +=1
    print(nums)
moveZeroes(nums)