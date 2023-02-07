# -*- coding: utf-8 -*-
# practical 0.1
# task ¹1
# olga volkova
# visual studio community 2022 17.4.4 (python 3.6.2)
# date of development: 07.02.2023
# program - triangle
# purpose: implementation methods(1. increasing/decreasing size of side; 2. calculation radius of circumscribed circle; 3. calculating perimeter; 4.determining values of angles.)
from math import acos, degrees, pow, sqrt  # calling mathematical functions


class triangle:  # class declaration
    def __init__(self, first, second):  # initializing objects
        self.first, self.second = first, second  # two teal numbers


    def increase_size_a(self, percent):  # changing size of first side
        return "Changed first side: " + str(round(self.first / 100 * percent + self.first, 3))


    def increase_size_b(self, percent):  # changing size of second side
        return "Changed second side: " + str(round(self.second / 100 * percent + self.second, 3))


    def r_circle(self):  # calculation radius of circumscribed circle
        return "Radius of circumscribed circle: " + str(round(pow(self.first, 2) / sqrt(4 * pow(self.first, 2) - pow(self.second, 2)), 3))


    def perimeter(self):  # calculating perimeter
        return "Perimeter of triangle: " + str(round(self.first * 2 + self.second, 3))


    def value_angles(self):  # determining values of angles
        return "Angles at base: " + str(round(degrees(acos(self.second / (self.first * 2))), 3)) + '\n' + "Angles opposite to base: " + str(round(180 - degrees(acos(self.second / (self.first * 2))) * 2, 3))


a, b = float(input("Entering first side: ")), float(input("Entering second side: "))  # entering two sides
# checking operability of all methods
print(triangle(a, b).increase_size_a(float(input("Entering percentage to change first side: "))))
print(triangle(a, b).increase_size_b(float(input("Entering percentage to change second side: "))))
print(triangle(a, b).r_circle())
print(triangle(a, b).perimeter())
print(triangle(a, b).value_angles())