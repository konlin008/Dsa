def merge(arr, l, m, r):
    temp=[] 
    left=l
    right=m+1
    while(left<=m and right<=r):
        if arr[left]< arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            right +=1
            
    while(left<=m):
        temp.append(arr[left])
        left +=1
        
    while(right<=r):
        temp.append(arr[right])
        right +=1
        
    for i in range(l,r+1):
        arr[i]= temp[i-l]
        
def mergeSort(arr, l, r):
    if l==r:
        return
    m= (l+r)//2
    mergeSort(arr,l,m)
    mergeSort(arr,m+1,r)
    merge(arr,l,m,r)

N = 10
arr=[10,9,8,7,6,5,4,3,2,1]    
mergeSort(arr, 0, 9)
print(arr)