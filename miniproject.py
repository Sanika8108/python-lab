# Student Management System Project in Python

students = {}


def add_student():
  student_id = input("Enter Student ID: ").strip()
  if student_id in students:
    print("❌ Error: Student ID already exists!")
    return

  name = input("Enter Student Name: ").strip()
  try:
    marks = float(input("Enter Student Marks (0-100): "))
    if marks < 0 or marks > 100:
      print("❌ Error: Marks must be between 0 and 100.")
      return
  except ValueError:
    print("❌ Error: Please enter a valid number for marks.")
    return

  students[student_id] = {"name": name, "marks": marks}
  print(f"✅ Student '{name}' added successfully!")


def view_students():
  if not students:
    print("\n📂 No student records found.")
    return

  print("\n" + "=" * 40)
  print(f"{'ID':<10} | {'Name':<20} | {'Marks':<10}")
  print("-" * 40)
  for sid, details in students.items():
    print(f"{sid:<10} | {details['name']:<20} | {details['marks']:<10}")
  print("=" * 40)


def search_student():
  student_id = input("Enter Student ID to search: ").strip()
  if student_id in students:
    info = students[student_id]
    print("\n🔍 Student Found:")
    print(f"ID     : {student_id}")
    print(f"Name   : {info['name']}")
    print(f"Marks  : {info['marks']}")
  else:
    print("❌ Student ID not found.")


def calculate_average():
  if not students:
    print("\n📂 No students available to calculate average.")
    return

  total_marks = sum(s["marks"] for s in students.values())
  avg_marks = total_marks / len(students)
  print(f"\n📊 Average Marks of {len(students)} student(s): {avg_marks:.2f}")


def delete_student():
  student_id = input("Enter Student ID to delete: ").strip()
  if student_id in students:
    removed = students.pop(student_id)
    print(f"🗑️ Student '{removed['name']}' deleted successfully!")
  else:
    print("❌ Student ID not found.")


def main():
  while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Calculate Average Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
      add_student()
    elif choice == "2":
      view_students()
    elif choice == "3":
      search_student()
    elif choice == "4":
      calculate_average()
    elif choice == "5":
      delete_student()
    elif choice == "6":
      print("👋 Exiting Student Management System. Goodbye!")
      break
    else:
      print("❌ Invalid choice. Please select an option from 1 to 6.")


if __name__ == "__main__":
  main()
