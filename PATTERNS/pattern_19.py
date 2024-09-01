def p19(n):
    def upper(n):
        for i in range(n):
            for j in range(n-i):
                print("*",end=" ")
            for s in range(i*2):
                print(" ", end=" ")
            for k in range(n-i): 
                print("*",end=" ")
            print()
    def lower(n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end=" ")
            for s in range(n*2-i*2):
                print(" ", end=" ")
            for k in range(i):
                print("*",end=" ")
            print()
    upper(n);
    lower(n)
        
p19(5)


#     * * * * * * 
#     * * - - * * 
#     * - - - - * 
#     * - - - - * 
#     * * - - * * 
#     * * * * * * 
