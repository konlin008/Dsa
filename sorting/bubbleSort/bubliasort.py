def bubli(arr):
    n=len(arr)
    swaped = 0
    for i in range (n,1,-1):
        for j in range(i-1):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaped =1
        if swaped ==0:
            break
    print(arr)
arr=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

bubli(arr)