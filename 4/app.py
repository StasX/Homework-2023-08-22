# Message for user input
msg = "Please enter a number: "

# Get user input
user_input = input(msg)
number = int(user_input)

# Loop until user entering non-negative number
while number >= 0:

    # Get power of number
    power = number**3

    # Print result
    print(f"{number} ** 3 = {power}")

    # Get user input
    user_input = input(msg)
    number = int(user_input)
