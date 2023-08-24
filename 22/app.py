# Print message for user
print("Enter numbers, for exit enter numbers smaller than 1")

# Init variable
number = 1

# Loop until user not entering 0 or negative number
while number > 0:

    # Get number from user
    user_input = input("Your number: ")
    number = int(user_input)

    # Print all numbers from entered number to 1
    for i in range(number, 0, -1):
        print(i, end=" ")
    print()
