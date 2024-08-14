def p14(n):
    for i in range(n):
        char='A'
        for j in range(i+1):
            print(char,end=" ")
            char = chr(ord(char) + 1) 
        print()
p14(5)