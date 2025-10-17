square = lambda a: a*a

rectangle = lambda l, b: l * b

triangle = lambda h, b: (h*b)/2

s =  int(input("Enter the side of square: "))

l =  int(input("Enter the length of the rectangle: "))

b = int(input("Enter the breadth of rectangle: "))

bt = int(input("Enter the breadth of triangle: "))

h = int(input("Enter the height of triangle: "))

print("Area of Square",square(s))
print("Area of Rectangle",rectangle(l, b))
print("Area of Triangle",triangle(bt, h))
