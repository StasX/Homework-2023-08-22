msg = "Please enter a number: "

user_input = input(msg)
number = int(user_input)

while number > 0:
    for i in range(number):
        for j in range(1, number+1):
            print(j, end=" ")

        print()

    user_input = input(msg)
    number = int(user_input)
