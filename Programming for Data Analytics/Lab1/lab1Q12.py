salary = float(input("Enter your salary: "))
age = int(input("Enter your age: "))
years_worked = int(input("How many years have you worked?: "))
has_kid = input("Do you have a child? (y/n): ")

if (salary > 40 and age > 25 or years_worked > 25):
    print("You can apply for a mortgage")
else:
    print("You cannot apply for a mortgage")

if (salary > 40 or age > 35 and years_worked >= 10 or has_kid == 'y'):
    print("You can apply for a mortgage")
else:
    print("You cannot apply for a mortgage")