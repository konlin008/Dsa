def triangle( N:int) ->None:
    for i in range(1,N+1):
        for j in range(i):
            print(i, end=" ")
        print()

    # Write your solution here.
    pass
triangle(5)