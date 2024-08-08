# def box(N):
#     for i in range(N):
#         for j in range(N):
#             print("*", end=" ")
#         print()
# box(5)q

def seeding(n: int) -> None:
    for i in range(n):
        for j in range(1,n-i+1):
            print(j, end=" ")
        print()
    pass
seeding(5)