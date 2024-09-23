# Find Kth Smallest Element Using Selection Sort

# Problem: Use selection sort to find the k-th smallest element in an array.
# Input: Array: [7, 10, 4, 3, 20, 15], k = 3
# Output: 7


def KthValue(arr,k):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i,n):
            if arr[j]<arr[min]: min=j
            temp=arr[min]    
            arr[min]=arr[i]
            arr[i]=temp
    print(arr[k-1])
arr=[7, 10, 4, 3, 20, 15]     
k=3
KthValue(arr,k)  

            