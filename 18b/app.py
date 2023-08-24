# Get area height from user
height_input = input("Please enter height (positive number): ")
height = int(height_input)

# Get area length from user
length_input = input("Please enter length (positive number): ")
length = int(length_input)

# Print area of *
for i in range(height):
    for j in range(length):
        print("*", end=" ")
    print()
