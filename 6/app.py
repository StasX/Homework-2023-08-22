# Print message to user
print("Please enter numbers...")

# Init a variable
number = 1

# Loop until user not entering 0
while number != 0:

    # Get user input
    user_input = input("Your number: ")
    number = int(user_input)

    # Detect number type
    if number < 0:
        result = "negative"
    elif number == 0:
        result = "0"
    else:
        result = "positive"

    # Output number type to user
    print("Your number is", result)
