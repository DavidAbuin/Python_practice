# Variable Scope

cm_per_inch = 2.54
inches_per_foot = 12

def height_US_to_cm(feet, inches):
    """ Converts a height in feet/inches to centimeters."""
    total_inches = (feet * inches_per_foot) + inches  # Total inches
    cm = total_inches * cm_per_inch
    return cm

#feet = int(input('Enter feet: '))
#inches = int(input('Enter inches: '))

feet = 5
inches = 10
print('Centimeters:', height_US_to_cm(feet, inches))

# Global statement allows modifying a global variable
employee_name = 'N/A'

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name

get_name()
print('Employee name:', employee_name)

# Mutable default objects remain changed over multiple function calls
def my_func(value, my_list=None):
    if my_list == None:
        my_list = []
    my_list.append(value)
    return my_list

numbers = my_func(50)  # default list appended with 50
print(numbers)
numbers = my_func(100)  # default list appended with 100
print(numbers)

#Arbitrary numbers of position arguments using *args.
def sandwich(bread, meat, *args):
    print('%s on %s' % (meat, bread), end=' ')
    if len(args) > 0:
        print('with', end=' ')
    for extra in args:
        print(extra, end=' ')
    print("")


sandwich('sourdough', 'turkey', 'mayo')
sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')

'''
turkey on sourdough with mayo
ham on wheat with mustard tomato lettuce
'''
# Arbitrary numbers of keyword arguments using **kwargs.
def sandwich(bread, meat, **kwargs):
    print('%s on %s' % (bread, meat))
    for category, extra in kwargs.items():
        print('   %s: %s' % (category, extra))

sandwich('sourdough', 'turkey', sauce='mayo')
sandwich('wheat', 'ham', sauce1='mustard', veggie1='tomato', veggie2='lettuce')

'''
sourdough on turkey
   sauce: mayo

wheat on ham
   veggie2: lettuce
   sauce1: mustard
   veggie1: tomato
'''

# Multiple function outputs
# Multiple outputs can be returned in a container
student_scores = [75, 84, 66, 99, 51, 65]


def get_grade_stats(scores):
    # Calculate the arithmetic mean
    mean = sum(scores) / len(scores)

    # Calculate the standard deviation
    tmp = 0
    for score in scores:
        tmp += (score - mean) ** 2
    std_dev = (tmp / len(scores)) ** 0.5

    # Package and return average, standard deviation in a tuple
    return mean, std_dev


# Unpack tuple
average, standard_deviation = get_grade_stats(student_scores)

print('Average score:', average)
print('Standard deviation:', standard_deviation)

# Multi-line docstrings can be used for more complicated functions to describe the function arguments.
# Multi-line docstrings should use consistent indentation for each line, separating the ending triple-quotes by a
# blank line. The following function definition illustrates:

def ticket_price(origin, destination, coach=True, first_class=False):
    """Calculates the price of a ticket between two airports.
    Only one of coach or first_class must be True.

    Arguments:
    origin -- string representing code of origin airport
    destination -- string representing code of destination airport

    Optional keyword arguments:
    coach -- Boolean. True if ticket cost priced for a coach class ticket (default True)
    first_class -- Boolean. True if ticket cost priced for a first class ticket (default False)

    """
    #Function body statements ...

    # help(ticket_price)
    '''Output is: 
    Help on function ticket_price in module __main__:

    ticket_price(origin, destination, coach=True, first_class=False)
    Calculates the price of a ticket between two airports.
    Only one of coach or first_class must be True.
    
    Arguments:
    origin -- string representing code of origin airport
    destination -- string representing code of destination airport
    
    Optional keyword arguments:
    coach -- Boolean. True if ticket cost priced for a coach class ticket (default True)
    first_class -- Boolean. True if ticket cost priced for a first class ticket (default False)

    '''
# The statement help(__name__) runs the help function on the global scope of the editor, printing information about all items defined there

# Trajectory of object on Earth


import math

def trajectory(t, a, v, g, h):
    '''The program's code asks the user for the object's initial velocity, angle, and height (y position),
    and then prints the object's position for every second until the object's y position is no longer greater than 0
    (meaning the object fell back to earth).'''
    """Calculates new x,y position"""
    x = v * t * math.cos(a)
    y = h + v * t * math.sin(a) - 0.5 * g * t * t
    return (x,y)

def degree_to_radians(degrees):
    """Converts degrees to radians"""
    return ((degrees * math.pi) / 180.0)

gravity = 9.81 # Earth gravity (m/s^2)
time = 1.0 # time (s)
x_loc = 0
h = 0

angle = float(input('Launch angle (deg): '))
print(angle)
angle = degree_to_radians(angle)

velocity = float(input('Launch velocity (m/s): '))
print(velocity)

height = float(input('Initial height (m): '))
y_loc = height
print(y_loc)

while ( y_loc >= 0.0 ): # While above ground
    print('Time %3d x = %3d y = %3d' % (time, x_loc, y_loc))
    x_loc, y_loc = trajectory(time, angle, velocity, gravity, height)
    time += 1.0

'''
Output of 45, 100, 3 is:
Launch angle (deg): 45.0
Launch velocity (m/s): 100.0
Initial height (m): 3.0
Time   1 x =   0 y =   3
Time   2 x =  70 y =  68
Time   3 x = 141 y = 124
Time   4 x = 212 y = 170
Time   5 x = 282 y = 207
Time   6 x = 353 y = 233
Time   7 x = 424 y = 250
Time   8 x = 494 y = 257
Time   9 x = 565 y = 254
Time  10 x = 636 y = 242
Time  11 x = 707 y = 219
Time  12 x = 777 y = 187
Time  13 x = 848 y = 145
Time  14 x = 919 y =  93
Time  15 x = 989 y =  31

Feedback?
participation activity
9.10.2: Projective location.
'''