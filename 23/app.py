user_input = input("Please enter a number: ")
number = int(user_input)

is_prime = number % 2 != 0

for i in range(3, int(number**0.5)+1, 2):
    if number % i == 0:
        is_prime = False
        break

result = "prime" if is_prime else "not prime"
print(number, " is a", result, "number")
