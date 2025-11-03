# prog2.py
from graphics.rectangle import area1, perimeter1
from graphics.circle import area as circle_area, perimeter as circle_perimeter
from graphics.graphics_3d.cuboid import surface_area, volume
from graphics.graphics_3d.sphere import surface_area1 as sphere_area1, volume1 as sphere_volume1

print("Rectangle area:", area1(10, 5))
print("Rectangle perimeter:", perimeter1(10, 5))

print("Circle area:", circle_area(7))
print("Circle perimeter:", circle_perimeter(7))

print("Cuboid surface area:", surface_area(2, 3, 4))
print("Cuboid volume:", volume(2, 3, 4))

print("Sphere surface area:", sphere_area1(5))
print("Sphere volume:", sphere_volume1(5))
