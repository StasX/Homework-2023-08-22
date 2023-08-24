# Get first number from user
first_input = input("Please enter first number: ")
first = int(first_input)

# Get second number from user
second_input = input("Please enter second number: ")
second = int(second_input)

# If first number greater than second then swap
if first > second:
    temp = first
    first = second
    second = temp

# Print numbers from first number to second number
for i in range(first, second+1):
    if (i % 10 == 7 or i % 7 == 0):
        print(i, end=" ")
