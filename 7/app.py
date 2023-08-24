# Print message to user
print("Please enter numbers...")

# Init a variable
number = 1

# Loop until user not entering negative number
while number >= 0:

    # Get user input
    user_input = input("Your number: ")
    number = int(user_input)

    # Get third power of number
    power = number ** 3

    # Output third power of number to user
    print(f"{number} ** 3 = {power}")
