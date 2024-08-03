# Day of the Week:
# Write a program that takes an integer (1-7) and uses match to return the corresponding day of the week (1 for Monday, 2 for Tuesday, etc.).
day=int(input("Enter The Day Number>>"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")