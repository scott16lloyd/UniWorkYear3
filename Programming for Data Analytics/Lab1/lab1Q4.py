student_forename = input("What is your forename?: ")
student_surname = input("What is your surname?: ")

math_grade = float(input('What grade did you get in maths?: '))
science_grade = float(input("What grade did you get in science?: "))
english_grade = float(input("What grade did you get in english?: "))
student_name = student_forename + " " + student_surname
average_grade = (math_grade + science_grade + english_grade) / 3
print(f"Name: {student_name} \n Your average grade is: {average_grade}")
