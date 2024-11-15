#brute
# nums =[4,1,2,1,2]
# def apearsOne(nums):
#     for i in nums:
#         flag=0
#         for j in nums:
#             if j==i:
#                 flag +=1
#         if flag==1:
#             print(i)     
# apearsOne(nums)   



#better
arr=[1,1,2,2,3,3,4,4,6]
def apones(arr):
    maxi=arr[0]
    for i in arr:
        maxi=max(maxi,i)+1
    hash=[0]*(maxi)
    for i in arr:
        hash[i]+=1
    for i in range(len(arr)):
        if hash[i]==1:
            print(i)
apones(arr)

#optimal

def apone(arr):
    xor=0
    for i in arr:
        xor=xor^i
    print(xor)
    
apone(arr)
    

