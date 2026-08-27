
name = input("Enter employee name: ")
role = input("Enter employee role: ")
salary = float(input("Enter monthly salary: "))

print("\n" + "=" * 35)
print("       EMPLOYEE IDENTITY CARD")
print("=" * 35)
print(f"Name          : {name}")
print(f"Role          : {role}")
print(f"Monthly Salary: ₹{salary:,.2f}")
print("=" * 35)
