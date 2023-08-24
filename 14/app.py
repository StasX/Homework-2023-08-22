# Print message to user
print("Enter two numbers (First should be smaller).")

# Get first number from user
first_input = input("Please enter first number: ")
first = int(first_input)

# Get second number from user
second_input = input("Please enter second number: ")
second = int(second_input)

# Print numbers from first number to second number
for i in range(first, second+1):
    print(i, end=" ")
