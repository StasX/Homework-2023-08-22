# Message for user input
msg = "Please enter a number: "

# Get user input
user_input = input(msg)
number = int(user_input)

# Loop until user entering non-negative number
while number % 7 != 0:

    # Detect if number negative positive or 0
    if number > 0:
        result = "positive"
    else:
        result = "negative"

    # Print result
    print(f"You entered {result} number.")

    # Get user input
    user_input = input(msg)
    number = int(user_input)
