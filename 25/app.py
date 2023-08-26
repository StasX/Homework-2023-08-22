print("Please enter 10 numbers")

for i in range(1, 11):
    user_input = input(f"Number #{i}: ")
    number = int(user_input)

    for _ in range(number):
        for j in range(1, number+1):
            print(j, end=" ")
        print()
