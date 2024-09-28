def findKthLargest(nums, k):
        l=len(nums)
        for i in range(l):
            j=i
            while(j>0 and nums[j]>nums[j-1]):
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j -=1
            print(f"When i {i} arr is {nums}")
        print(nums[k-1])
        return nums[k]
nums =[3,2,1,5,6,4]
k =2
findKthLargest(nums, k)