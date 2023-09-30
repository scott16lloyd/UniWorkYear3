class_a_number_sold = int(input("How many class A tickets were sold?: "))
class_b_number_sold = int(input("How many class B tickets were sold?: "))
class_c_number_sold = int(input("How many class C tickets were sold?: "))

total_income = (class_a_number_sold * 25) + \
    (class_b_number_sold * 20) + (class_c_number_sold * 30)

print(f"Total income: ${total_income}")
