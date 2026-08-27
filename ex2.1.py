
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))


total = mark1 + mark2 + mark3
average = total / 3


print("\n===== FINAL SCORECARD =====")
print(f"Subject 1 Marks: {mark1}")
print(f"Subject 2 Marks: {mark2}")
print(f"Subject 3 Marks: {mark3}")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print("===========================")
