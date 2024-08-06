# Write a function is_even(n) that takes an integer as an argument and returns True if the number is even, otherwise False.
def even_checker(num):
    if num != 0:
        if num % 2 == 0:
            print("The Number IS Even")
        else:
            print("The Number Is not Even")
    else:
        print("The Number Is: 0")  
even_checker(0)