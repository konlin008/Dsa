#brute
nums =[4,1,2,1,2]
def apearsOne(nums):
    for i in nums:
        flag=0
        for j in nums:
            if j==i:
                flag +=1
        if flag==1:
            print(i)     
apearsOne(nums)   