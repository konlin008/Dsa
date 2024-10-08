arr = [1, 8, 7, 56, 5,12,45]
largest = arr[0]
sLargest = -1



def findSecondLargest(arr,largest,sLargest):
    for elm in arr:
        if elm>largest:
            sLargest = largest
            largest = elm
        elif elm<largest and elm>sLargest:
            sLargest = elm
    print(sLargest)        
    
findSecondLargest(arr,largest,sLargest)
