# Get number from user
user_input = input("Please enter positive number: ")
number = int(user_input)

# Print square of numbers
for i in range(number):
    for j in range(number, 0, -1):
        print(j, end=" ")
    print()
