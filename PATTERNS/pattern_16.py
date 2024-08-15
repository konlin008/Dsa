def p15(n):
    char='A'
    for i in range(n):
        for j in range(i+1):
            print(char, end=" ")
        char = chr(ord(char) + 1)
        print()
p15(5)