# def p16(n):
#     for i in range(n):
#         for j in range(n+1-i):
#             print("-",end="")
#         char='A'
#         for l in range(i*2+1):
#             print(char,end="-") 
#             if(l==i):
#                 char = chr(ord(char) - 1) 
#             else:
#                 char = chr(ord(char) + 1) 
#         for k in range(n-i):
#             print("-",end="")
#         print()
# p16(3)

n = 3
for i in range(n):
    for j in range(n + 1 - i):
        print(" ", end="")
    char = 'A'
    for l in range(2 * i + 1):
        print(char, end=" ")
        if l < i:
            char = chr(ord(char) + 1)  
        else:
            char = chr(ord(char) - 1)  
    for k in range(n - i):
        print(" ", end="")
    print()  