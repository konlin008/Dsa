def p20(n):
    for i in range(1,n*2):
            if(i<=n):
                for j in range(i):
                    print("*",end=" ")
                for s in range(n*2-i*2):
                    print(" ", end=" ")
                for k in range(i):
                    print("*",end=" ")
            else:
                for j in range(n*2-i):
                    print("*",end=" ")
                for s in range((i-n)*2):
                    print(" ", end=" ")
                for k in range(n*2-i):
                    print("*",end=" ")
            print()
            
p20(5)