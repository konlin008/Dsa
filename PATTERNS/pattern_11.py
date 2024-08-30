def p11(n):
    for i in range(1,n+1):
        star=1
        if(i%2 != 0):
            star=1
        else:
            star=0
        for j in range(i):
            print(star, end=" ")
            star=1-star
        print()
p11(5)


