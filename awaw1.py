def circumference(radius):
    pi = 3.14159
    return 2 * pi * radius
r = float(input("Enter the radius of the circle: "))
c = circumference(r)
print("The circumference of the circle is:",c)