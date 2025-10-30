from database import add_student, view_students, search_student
from utils import print_menu
def main():
    while True:
        choice = print_menu()
        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.\n")
if __name__ == "__main__":
    main()