# Given an Integer n and a list arr. Sort the array using bubble sort algorithm.

# Examples :

# Input: n = 5, arr[] = {4, 1, 3, 9, 7}
# Output: 1 3 4 7 9
# Input: n = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
# Output: 1 2 3 4 5 6 7 8 9 10

def bubble_sort(arr):
    n=len(arr)
    for i in range(n,1,-1):
        swapCount=0
        for j in range(i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapCount=1
        if(swapCount==0):break
    print(arr)
arr=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(arr)