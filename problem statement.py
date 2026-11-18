
def check_tri(a, b, c):
    if a*a + b*b == c*c:
        return "Right angled triangle"
    else:
        return "Not a right angled triangle"

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# Arrange sides in ascending order
sides = sorted([a, b, c])

print(check_tri(sides[0], sides[1], sides[2]))
