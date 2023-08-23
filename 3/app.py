# Set message for number input
msg = "Please enter a number: "

# Print to user to enter numbers...
print("Please enter numbers. For exit enter 0")

# Get number from user
user_input = input(msg)
number = float(user_input)

# Run until user not entering 0
while number != 0:
    # Detect if a number negative
    result = "negative" if number < 0 else "positive"
    print("You entered", result, "number")

    # Get number from user
    user_input = input(msg)
    number = float(user_input)
