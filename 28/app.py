for i in range(1, 11):
    first_input = input(f"Please enter a first number in pair #{i}: ")
    first = int(first_input)
    second_input = input(f"Please enter a second number in pair #{i}: ")
    second = int(second_input)
    max_number = first if first >= second else second
    print(f"Max number for pair #{i} is {max_number}")
