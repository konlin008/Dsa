def p15(n):
    for i in range(n):
        char='A'
        for j in range(n-i):
            print(char, end=" ")
            char = chr(ord(char) + 1)
        print()
        
p15(5)