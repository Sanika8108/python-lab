

grades = [85, 72, 90, 68, 95]

print("Current grades:", grades)


index = int(input("Enter the index position to update: "))


new_grade = int(input("Enter the new grade: "))


if 0 <= index < len(grades):
    grades[index] = new_grade
    print("Updated grades:", grades)
else:
    print("Invalid index. Please enter a valid position.")
