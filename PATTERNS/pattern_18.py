def p18(n):
    for i in range(n):
        char= "A"
        char = chr(ord(char) + n-1)
        for j in range(i+1):
            print(char, end=" ")
            char = chr(ord(char) -1)  
        print()
        
p18(5)