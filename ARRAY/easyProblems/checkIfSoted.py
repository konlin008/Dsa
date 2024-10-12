arr = [1,2,3,4,5,6]
arr2 = [3,4,5,1,2]
arr3 = [2,1,3,4]
arr4 = [1,2,3]
def checkIfSOrted(arr):
    count = 0
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            print("Array is not Sorted")
            
    print("Array is Sorted")        
checkIfSOrted(arr)
checkIfSOrted(arr2)
checkIfSOrted(arr3)
checkIfSOrted(arr4)