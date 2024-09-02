def p22(n):
    for i in range(n*2-1):
        for j in range(n*2-1):
            if(i==0 or i==n*2-2 or j==0 or j==n*2-2):
                print(n,end="")
            else:
                print(n-1, end="")
        print()
        
p22(5)