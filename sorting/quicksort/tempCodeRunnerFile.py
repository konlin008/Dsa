pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<= pivot and i<=high -1:
            i +=1
            while arr[j]> pivot and j>=low +1:
                j -=1 
            if i<j:
                arr[i],arr[j] = arr[j], arr[i]
    arr[low],arr[j]= arr[j],arr[low] 
    return j       