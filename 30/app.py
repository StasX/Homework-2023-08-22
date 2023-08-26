
# Get count from user
user_input = input("Please enter count: ")
count = int(user_input)

for _ in range(count):
    # Get first number from user
    first_input = input("Please enter first number: ")
    first = int(first_input)

    # Get second number from user
    second_input = input("Please enter second number: ")
    second = int(second_input)

    # Get third number from user
    third_input = input("Please enter third number: ")
    third = int(third_input)

    # find max
    max_number = first if first > second else second
    max_number = third if third > max_number else max_number

    # Print max number to user
    print("Max number is:", max_number)
