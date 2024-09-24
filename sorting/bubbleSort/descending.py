# Modify the bubble sort algorithm to sort an array of integers in descending order.
# Input: n = 5, arr[] = {4, 1, 3, 9, 7}
# Output: 9,7,4,3,1


def descendingSort(arr):
    n=len(arr)
    for i in range(n,1,-1):
        swapCount=0
        for j in range(i-1):
            if arr[j]< arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapCount+=1
        if swapCount==0:break
    print(arr)
arr=[4, 1, 3, 9, 7]    
descendingSort(arr)    