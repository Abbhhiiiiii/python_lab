import graphics.rectangle
import graphics.circle

import graphics.graphics_3d.cuboid as cuboid

import graphics.graphics_3d.sphere as sphere

print("Rectangle area:", graphics.rectangle.area1(10, 5))

print("Rectangle perimeter:", graphics.rectangle.perimeter1(10, 5))

print("Circle area:", graphics.circle.area(7))

print("Circle perimeter:", graphics.circle.perimeter(7))

print("Cuboid surface area:", cuboid.surface_area(2, 3, 4))

print("Cuboid volume:", cuboid.volume(2, 3, 4))

print("Sphere surface area:", sphere.surface_area1(5))
print("Sphere volume:", sphere.volume1(5))
