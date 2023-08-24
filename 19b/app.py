# Get number from user
user_input = input("Please enter positive number: ")
number = int(user_input)

# Print triangle of *
for i in range(number, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
