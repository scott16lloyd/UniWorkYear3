m1 = float(input("Enter the first object mass: "))
m2 = float(input("Enter the second object mass: "))
r = float(input("Enter the shortest distance to these objects: "))

universal_gravitation = 9.8 * ((m1 * m2) / r)

print(f"Universal gravitation = {universal_gravitation}")
