students = []
def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    student = {"name": name, "roll": roll, "course": course}
    students.append(student)
    print("Student added successfully!\n")
def view_students():
    print("\n--- View Students ---")
    if not students:
        print("No students found!\n")
        return
    for i, s in enumerate(students, start=1):
        print(f"{i}. Name: {s['name']}, Roll: {s['roll']}, Course: {s['course']}")
    print()
def search_student():
    print("\n--- Search Student ---")
    keyword = input("Enter name or roll number to search: ")
    found = False
    for s in students:
        if keyword.lower() in s["name"].lower() or keyword == s["roll"]:
            print(f"Found → Name: {s['name']}, Roll: {s['roll']}, Course: {s['course']}")
            found = True
    if not found:
        print("No matching student found.\n")
    print()
