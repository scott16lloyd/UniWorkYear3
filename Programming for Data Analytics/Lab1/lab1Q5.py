weight = float(input("Enter your weight (pounds): "))
height = float(input("Enter your height (inches): "))

BMI = (weight/height**2) * 703
print(f"Your BMI is: {BMI}")
