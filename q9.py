# Python program to print area and perimeter of various geometry by inheriting 
# polygon class
from math import tan, pi

class Polygon:
    def __init__(self,shape):
        self.shape = shape
    def get_area(self,side):
        return "{:.5f}".format(self.shape * (side ** 2) / (4 * tan(pi / self.shape)))
    def get_perimeter(self,side):
        return self.shape * side

square = Polygon(4)
pentagon = Polygon(5)

print(pentagon.get_perimeter(12))
print(square.get_area(20))