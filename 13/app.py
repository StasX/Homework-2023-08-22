# Get number from a user
user_input = input("Please a positive number: ")
number = int(user_input)

# Display numbers from 1 to number
for i in range(1, number+1):
    print(i, end=" ")
# Display numbers from number to 1
for i in range(number, 0, -1):
    print(i, end=" ")
