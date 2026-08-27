
status = input("Enter atmospheric status (hot/cold/normal): ").lower()


if status == "hot":
    recommendation = "Turn on AC"
elif status == "cold":
    recommendation = "Activate heater"
elif status == "normal":
    recommendation = "Idle"
else:
    recommendation = "Unknown atmospheric status"


print("\n===== CLIMATE MONITORING =====")
print(f"Atmospheric Status: {status}")
print(f"Hardware Recommendation: {recommendation}")
print("==============================")
