print("Please enter 10 numbers")

for i in range(1, 11):
    user_input = input(f"Number #{i}: ")
    number = int(user_input)

    for _ in range(number):
        print("* " * number)
    print()
