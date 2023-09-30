# For loops and functions
# 1
def times_tables():
    num = int(input("Please enter a times tables for printing: "))
    limit = int(input("Please enter upper limit for multiplication: "))

    for index in range(limit):
        calculation = index * num
        print(f"{num} * {index} = {calculation}")


def print_num_triangle():
    num = int(input("Enter an integer for the triangle size: "))

    for i in range(num + 1):
        for j in range(i):
            print(i, end="")
        print()

# 2


def print_rainfall():
    months = int(input("How many months of data do you wish to enter: "))
    rainfall = []
    highest_rainfall = 0
    average_rainfall = 0
    total = 0

    for index in range(months):
        rain = float(input(f"Please enter rainfall for month {index + 1}: "))
        rainfall.append(rain)

    for value in rainfall:
        if value > highest_rainfall:
            highest_rainfall = value

    for index in range(len(rainfall)):
        total += rainfall[index]

    average_rainfall = total / months

    print(f"Highest rainfall value: {highest_rainfall}")
    print(f"Average is {average_rainfall}")

# Q3


def fibonacci_sequence():
    limit = 40
    fib_nums = [0, 1]

    def calculation(fib_nums):
        fib_nums = [0, 1]
        for index in range(limit):
            calc = fib_nums[index+1] + fib_nums[index]
            fib_nums.append(calc)
        print(fib_nums)

    calculation(fib_nums)

    limit = int(input("Select a integer between 1-14: "))

    while (limit < 1 or limit > 14):
        limit = int(input("Select a integer between 1-14: "))

    calculation(fib_nums)

# Q4


def basic_calculator():
    number_one = int(input("Please enter a numberical value: "))
    number_two = int(input("Please enter a numberical value: "))
    result = 0

    def addition(number_one, number_two):
        result = number_one + number_two
        print(f"Addition of {number_one} and {number_two} is {result}")

    def subtraction(number_one, number_two):
        result = number_one - number_two
        print(f"Subtraction of {number_one} and {number_two} is {result}")

    def multiplication(number_one, number_two):
        result = number_one * number_two
        print(f"Multiplication of {number_one} and {number_two} is {result}")

    def division(number_one, number_two):
        result = number_one / number_two
        print(f"Division of {number_one} and {number_two} is {result}")

    user_input = 0

    while (user_input < 1 or user_input > 4):
        print("Would you like to perform:")
        print("1: Additon")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        user_input = int(input("Select 1-4:"))

    if (user_input == 1):
        addition(number_one, number_two)
    elif (user_input == 2):
        subtraction(number_one, number_two)
    elif (user_input == 3):
        multiplication(number_one, number_two)
    elif (user_input == 4):
        division(number_one, number_two)

# Q7


def prime_number_calculator(number):
    if (number % number == 0):
        print(f"{number} is a prime number.")
    elif (number % 1 == 0):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


# Main
prime_number_calculator(6)
