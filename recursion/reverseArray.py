def reverseArray(arr,start,end):
    if(start>=end):
        return
    else:
        arr[start],arr[end]=arr[end],arr[start]
        reverseArray(arr,start+1,end-1)
arr=[1,2,3,4,5,6]       
reversedArray=reverseArray(arr,0,5)
print(arr)