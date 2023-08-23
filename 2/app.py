# Get number from user
input_number = input("Please enter a number: ")

# Cast to integer
number = int(input_number)

# Check if last digit of entered number is a 5
result = "is 5" if number % 10 == 5 else "isn't 5"

# Print the result
print("Last digit of entered number", result)
