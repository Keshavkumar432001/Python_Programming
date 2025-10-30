def print_menu():
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Please enter a valid number.\n")
        return 0