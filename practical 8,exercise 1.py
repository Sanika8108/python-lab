def sanitize_name(first_name, last_name):
    # Remove leading/trailing whitespace, then apply title case
    first = first_name.strip().title()
    last = last_name.strip().title()

    return f"{first} {last}"


# Read user-submitted names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Sanitize and output the full name
full_name = sanitize_name(first_name, last_name)

print("Clean name:", full_name)
