arr = [1, 8, 7, 56, 5,12,45]
def findLargestElement(arr):
    maxElm = arr[0]
    for elm in arr:
        if elm >maxElm: 
            maxElm = elm
    print(maxElm)
findLargestElement(arr)