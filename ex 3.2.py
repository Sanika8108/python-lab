
score = float(input("Enter graduation score (%): "))
backlogs = int(input("Enter number of active academic backlogs: "))


if score >= 70 and backlogs == 0:
    print("\nCandidate is ELIGIBLE for placement.")
else:
    print("\nCandidate is NOT ELIGIBLE for placement.")


print("\n===== PLACEMENT ELIGIBILITY =====")
print(f"Graduation Score: {score:.2f}%")
print(f"Active Backlogs: {backlogs}")
print("=================================")
