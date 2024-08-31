# def p1(n):
#     for i in range(n):
#         for j in range(1,n-i+1):
#             print(j, end=" ")
#         print()
        
# p1(5)
#pattern 7
# def p7(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ",end="")
#         for z in range(i*2+1):
#             print("*",end="")
#         # for x in range(n-i-1):
#         #     print(" ",end="")
#         print()
# def p8(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for k in range(n*2-(2*i+1)):
#             print("*", end="")
#         for m in range(i):
#             print(" ",end="")
#         print()
        
# p7(3)
# p8(3)
# n=int(input("Enter A Number"))
# def p10(n):
#     for i in range(n*2-1):
#         if(i<n):
#             for j in range(i+1):
#                 print("*", end=" ")
#         else:
#             for j in range(n*2-i-1):
#                 print("*", end=" ")
#         print()
        
# p10(n)  



# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


# def p11(n):
#     for i in range(1,n+1):
#         star=1
#         if(i%2 != 0):
#             star=1
#         else:
#             star=0
#         for j in range(i):
#             print(star, end=" ")
#             star=1-star
#         print()
# p11(5)

#  1             1 
#  1 2         2 1 
#  1 2 3     3 2 1 
#  1 2 3 4 4 3 2 1 

# 1*-*-*-*-*1 
# 1*2*-*-*2*1 
# 1*2*3*3*2*1 


# def p12(n):
#     space=2*(n-1)
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j, end=" ")
#         for sp in range(space):
#             print(" ", end=" ")
#         space -= 2
#         for k in range(i,0,-1):
#             print(k, end=" ")
#         print()
# p12(4)

# def p13(n):
#     num=1
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(num, end=" ")
#             num+=1
#         print()
        
# p13(5)

# def p14(n):
#     for i in range(n):
#         char='A'
#         for j in range(i):
#             print(char, end="")
#             char = chr(ord(char) + 1)    
#         print()
        
# p14(5)
# def p15(n):
#     for i in range(n):
#         char='A'
#         for j in range(n-i):
#             print(char, end=" ")
#             char = chr(ord(char) + 1)    
#         print()
        
# p15(5)
# def p16(n):
#     char='A'
#     for i in range(1,n+1):  
#         for j in range(i):
#             print(char, end=" ")
#         char = chr(ord(char) + 1)   
#         print()
 
# p16(5)

