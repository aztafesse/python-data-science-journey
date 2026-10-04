students = {
    "Aziz":[88, 92, 79],
    "Ali": [75, 80, 68],
    "Sara": [95, 98, 92]
}

def show_menu():
    print("\n=== Student Grade Manager ===")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Class statistics")
    print("5. Delete student")
    print("6. Quit")

students = {}

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        name = input("Enter student name: ").strip().title()
        if name in students:
            print(f"{name} already exist. Use option to add garde instead.")
            continue

        grades_input = input("Enter grades separated by commas (e.g. 88,92,79): ")
        grades = []
        for g in grades_input.split(","):
            try:
                grades.append(float(g.strip()))
            except ValueError:
                print(f"Skipping invald garde:{g}")

        if grades:
            students[name] = grades
            print(f"Added {name} with grades {grades}")
        else:
            print("No valid grades entered")

    elif choice == "2":
        if not students:
            print("No students yet.")
            continue

        print("\n--- All Students ---")
        for name, grades in students.items():
            avg = sum(grades)/len(grades)
            print(f"{name}: grades={grades}, average={avg:.2f}")
            
    elif choice == "3":
        name = input("Enter student name: ").strip().title()
        if name in students:
            grades = students[name]
            avg = sum(grades)/len(grades)
            print(f"\n{name}:")
            print(f"    Grades: {grades}")
            print(f"    Average: {avg:.2f}")
            print(f"    Highest: {max(grades)}")
            print(f"    Lowest: {min(grades)}")
        else:
            print(f"{name} not found.")
    elif choice == "4":
        if not students:
            print("No students yet.")
            continue
        averages = {name: sum(g)/len(g) for name,g in students.items()}
        best = max(averages, key=averages.get)
        worst = min(averages, key=averages.get)
        class_avg = sum(averages.values())/len(averages)

        print("\n--- Class Statistics ---")
        print(f"Number of students: {len(students)}")
        print(f"Class average: {class_avg:.2f}")
        print(f"Top student: {best} ({averages[best]:.2f})")
        print(f"Lowest student: {worst} ({averages[worst]:.2f})")

    elif choice == "5":
        name = input("Enter student name to delete: ").strip().title()
        if name in students:
            del students[name]
            print(f"Deleted {name}.")
        else:
            print(f"{name} not found.")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

    
