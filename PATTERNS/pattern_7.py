def p7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for z in range(i*2+1):
            print("*",end="")
        # for x in range(n-i-1):
        #     print(" ",end="")
        print()
        
p7(4)

#    *   
#   ***  
#  ***** 
# *******