# Get number from user
user_input = input("Please enter positive number: ")
number = int(user_input)

# Print rectangle of numbers
for i in range(1, number+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
