
# Init variable
first = 1
second = 2

# Loop until user not entering two same numbers
while first != second:

    # Get from user first number
    first_input = input(f"Please enter a first number: ")
    first = int(first_input)

    # Get from user second number
    second_input = input(f"Please enter a second number: ")
    second = int(second_input)

    # Find max number
    max_number = first if first >= second else second

    # Print max number to user
    print(f"Max number is {max_number}")
