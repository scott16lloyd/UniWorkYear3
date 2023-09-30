salary = float(input("Enter your salary: "))
has_kids = (input("Do you have kids? (y/n)"))

if has_kids == "y":
    has_kids = True
elif has_kids == "n":
    has_kids = False

if (salary >= 30 and salary < 50 and has_kids == False):
    tax = 40
elif (salary >= 30 and salary < 50 and has_kids == True):
    tax = 35
elif (salary >= 50 and salary < 70 and has_kids == False):
    tax = 50
elif (salary >= 50 and salary < 70 and has_kids == True):
    tax = 45
elif (salary < 30):
    tax = 0
elif (salary >= 70):
    tax = 55
