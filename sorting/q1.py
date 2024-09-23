# 2. Sort an Array in Descending Order
# Modify the selection sort algorithm to sort an array in descending order.

# Input: [29, 10, 14, 37, 13]
# Output: [37, 29, 14, 13, 10]


def sort(arr):
    n=len(arr)
    for i in range(n):
        max=i
        for j in range(i,n):
            if arr[j]>arr[max]: max=j
        temp=arr[max]
        arr[max]=arr[i]
        arr[i]=temp
    print(arr)
    
arr=[29, 10, 14, 37, 13]
sort(arr)
        