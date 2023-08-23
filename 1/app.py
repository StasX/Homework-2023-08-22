# Get input from user
first_input = input("Please enter a first number: ")
second_input = input("Please enter a second number: ")

# Cast input to int
first = int(first_input)
second = int(second_input)

# Find the min number
minimum = first if first < second else second

# Print the result
print(f"The minimal number is {minimum}")
