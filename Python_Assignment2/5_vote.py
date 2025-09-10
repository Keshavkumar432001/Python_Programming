## Q5 Write a program to check whether a person is eligible to vote or not. (A person is eligible if their age is 18 or above).

age = int(input("Enter your age: "))

# Check age of a person is greater than or equal to 18
if age >= 18:
    # If condition is true, the person is eligible to vote
    print("You are eligible to vote.")
else:
    # If condition is false, the person is not eligible to vote
    print("You are not eligible to vote. You must be at least 18 years old.")