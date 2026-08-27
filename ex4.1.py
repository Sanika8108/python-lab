
status = input("Enter order status (shipped/delivered/pending): ").lower()

if status == "shipped":
    message = "Your order has been shipped and is on its way."
elif status == "delivered":
    message = "Your order has been delivered successfully. Thank you for shopping with us!"
elif status == "pending":
    message = "Your order is currently pending and will be processed soon."
else:
    message = "Sorry, the order status is not recognized. Please check again."


print("\n===== ORDER TRACKING UPDATE =====")
print(message)
print("=================================")
