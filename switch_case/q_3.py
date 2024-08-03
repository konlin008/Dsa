# Grade Categorization:
# Write a function that takes a letter grade ('A', 'B', 'C', 'D', 'F') and uses match to return a description (e.g., 'A' for "Excellent", 'B' for "Good", etc.).

grade=input("Enter Your Grade(A,B,C,D)>>")
grade=grade.lower()
match grade:
    case 'a':
        print("Excellent")
    case 'b':
        print("Good")
    case 'c':
        print("Avarage")
    case 'd':
        print("Poor")
    case 'e':
        print("Fail")
    case _:
        print("Enter a Vaild Grade")