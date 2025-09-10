## Q7 Write a program that takes marks as input and prints:  - 'Pass' if marks are 40 or above  - 'Fail' if marks are less than 40.
marks = int(input("Enter your marks: "))

# Check if marks are 40 or above
if marks >= 40:
    # If condition is true then student passes
    print("Pass")
else:
    # If condition is false than student fails
    print("Fail")