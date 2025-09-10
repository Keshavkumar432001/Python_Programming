## Q9 Write a program to input a character and check whether it is an uppercase letter, lowercase letter, or not a letter.

char = input("Enter a character: ")

# Checking only one character is entered or not
if len(char) != 1:
    print("Please enter only one character.")
else:
    # Check if the character is an uppercase letter
    if char >= 'A' and char <= 'Z':
        print(f"{char} is an uppercase letter.")

    # Check if the character is a lowercase letter
    elif char >= 'a' and char <= 'z':
        print(f"{char} is a lowercase letter.")

    # If not in A-Z or a-z then it is not a letter
    else:
        print(f"{char} is not a Letter.")
