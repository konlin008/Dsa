arr=[12,46,8,1,54,8]
n=len(arr)
print(n)
def sort(arr,n):
    for i in range(n):
        min=i
        for j in range(i,n):
            if arr[j]<arr[min]: min=j
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp
        print(arr)
    print(arr)

sort(arr,n)