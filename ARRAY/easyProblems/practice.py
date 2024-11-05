# def getSecondLargest( arr):
#     largElm=arr[0]
#     sLargElm= -1
#     for elm in arr:
#         if elm > largElm:
#             sLargElm = largElm
#             largElm = elm
#         elif elm > sLargElm and elm<largElm:
#             sLargElm = elm
#     print(sLargElm)
# arr = [10, 10]
# getSecondLargest(arr)

# arr = [1,2,3,4,5]
# def checkarr(arr):
#     for i in range(1,len(arr)):
#         if arr[i] < arr[i-1]:
#             print("Unsorted")
#             return
#     print("sorted")
# checkarr(arr)

# nums = [3,4,5,1,2]
# nums1 = [2,1,3,4]
# nums2 = [1,2,3]

# def check(nums):
#     count = 0
#     n = len(nums)
#     for i in range(n):
#         if nums[i]> nums[(i+1) % n]:
#             count +=1
#             if count>1:
#                 print(False)
#                 return
#     print(True)
# check(nums)
# check(nums1)
# check(nums2)


# arr=[0,0,1,1,1,2,2,3,3,4]

# def removeDup(arr):
#     i=0
#     for j in range(len(arr)):
#         if arr[j] != arr [i]:
#             i+=1
#             arr[i] = arr[j]
          
            
#     print(arr[:i+1])
    
# removeDup(arr)

arr = [1,2,3,4,5,6,7]

def leftRoatedOne(arr):
    temp= arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]= temp
    print(arr)
leftRoatedOne(arr)