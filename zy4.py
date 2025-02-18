def compute_square(num_to_square):
    return num_to_square * num_to_square

num_squared = 0
num_squared = compute_square(7)

print('7 squared is', num_squared)

import math

def square_root(x):
    return math.sqrt(x)

def print_val(x):
    print(x)
    return

cm_per_inch = 2.54
inches_per_foot = 12

def height_US_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters"""
    total_inches = feet * inches_per_foot + inches
    cm = total_inches * cm_per_inch
    return cm

#feet = int(input('Enter feet: '))
#inches = int(input('Enter inches: '))

#print('Centimeters:', height_US_to_cm(feet, inches))

def find_max(num1, num2):
    max_val = 0.0
    if (num1 > num2):
        max_val = num1
    else:
        max_val = num2
    return max_val

num_a = 5.0
num_b = 10.0
num_y = 3.0
num_z = 7.0
max_sum = 0.0

max_sum = find_max(num_a, num_b)
max_sum += find_max(num_y, num_z)

print('max_sum is', max_sum)

def pyramid_volume (base_length, base_width, pyramid_height):
    return base_length * base_width * pyramid_height* (1/3)

base_length = 4.5
base_width = 2.1
pyramid_height = 3.0

print ('Volume for %.2f %.2f %.2f is: %.2f' % (base_length, base_width, pyramid_height, pyramid_volume(base_length, base_width, pyramid_height) ))

print()

# Stopping the program using NotImplementedError in a function stub
import math


#def get_points(num_points):
  #  """Get num_points from the user. Return a list of (x,y) tuples."""
  #  raise NotImplementedError


def side_length(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def get_perimeter_length(points):
    perimeter = side_length(points[0], points[1])
    perimeter += side_length(points[0], points[2])
    perimeter += side_length(points[1], points[2])
    return perimeter


#coordinates = get_points(3)
#print('Perimeter of triangle:', get_perimeter_length(coordinates))