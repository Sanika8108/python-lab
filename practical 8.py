# ==================================================
# customer feedback formatter
# Teaching: Built-in string methods & string Formatting
# =====================================================
raw_name = input("Enter customer name: ")
raw_feedback = input(" Enter customer feedback massage: ")
rating = input("Enter reating(1 to 5): ")

clean_name =raw_name.strip()
clean_feedback=raw_feedback.strip()

formatted_name=clean_name.title()

formatted_feedback=clean_feedback.capitalize()
formatted_feedback=formatted_feedback.replace("u", "you").replace("r","are")

exclamation_count=formatted_feedback.count("!")

if int(rating) >=4:
    category= "POSITIVE".upper()
else:
    category = "NEEDS REVIEW".upper()

print("\n" + "=" * 45)
print(f"{'PROFESSIONAL FEEDBACK REPORT':^45}")
print("="*45)

print(f"customer name: {formatted_name}")
print(f"Rating       :{rating} / 5 stars")
print(f"category:     [{category}]")
print(f"Excitement:    {exclamation_count} exclamation mark(s)")
print("="* 45)
print("Formatted Massage:")
print(f'"{formatted_feedback}"')
print("="*45)