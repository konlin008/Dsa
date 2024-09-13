def nto1(n):
    if(n<1):return
    print(n)
    n-=1
    nto1(n)   
nto1(5)