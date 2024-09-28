
def insert( alist, index, n):
    j=index
    while(j>0 and alist[j]< alist[j-1]):
        alist[j],alist[j-1]=alist[j-1],alist[j]
        j-=1
    
def insertionSort( alist, n):
    for i in range(n):
        insert(alist,i,n)
    print(alist)
alist=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = 10
insertionSort(alist,n)