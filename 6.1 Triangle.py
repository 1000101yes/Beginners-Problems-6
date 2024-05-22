def triangleTest(x, y, z):
    if x > y and x > z:
        maximum = x
        side1 = y
        side2 = z
    if y > x and z > x:
        maximum = y
        side1 = x
        side2 = z
    if z > x and z > y:
        maximum = z
        side1 = x
        side2 = y
    sumSides = side1+side2
    if sumSides > maximum:
        return True
    else:
        return False

answer = triangleTest(5, 8, 10)
print(answer)
