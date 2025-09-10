## Q8 Write a program to check whether a given number is a multiple of 5.

num = int(input("Enter a number: "))

# A number is a multiple of 5 if the remainder is 0 when divided by 5
if num % 5 == 0:
    # If condition is true than number is multiple of 5
    print(f"{num} is a multiple of 5.")
else:
    # If condition is false than number is not multiple of 5
    print(f"{num} is NOT a multiple of 5.")