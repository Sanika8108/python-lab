
age = int(input("Enter your age: "))
income = float(input("Enter your annual family income ($): "))


if age < 25 and income < 300000:
    print("\nCongratulations! You qualify for the specialized education scholarship.")
else:
    print("\nSorry, you do not qualify for the specialized education scholarship.")


print("\n===== SCHOLARSHIP SCREENING =====")
print(f"Age: {age}")
print(f"Annual Family Income: ${income:,.2f}")
print("=================================")
