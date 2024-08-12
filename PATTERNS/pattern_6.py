def seeding(n: int) -> None:
    for i in range(n):
        for j in range(1,n-i+1):
            print(j, end=" ")
        print()
    pass
seeding(5)