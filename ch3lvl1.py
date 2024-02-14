import math
def triangle_area(a,b,c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area
a = triangle_area(3, 4, 5)
print(a)
