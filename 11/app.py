# Get number from a user
user_input = input("Please a positive number: ")
number = int(user_input)

# Display numbers between 1 and number
for i in range(1, number + 1):
    print(i, end=" ")
