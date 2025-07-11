# Base Classes and Inheritance

class TransportMode:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def info(self):
        print('%s can go %d mph.' % (self.name, self.speed))

class MotorVehicle(TransportMode):
    def __init__(self, name, speed, mpg):
        TransportMode.__init__(self, name, speed)
        self.mpg = mpg
        self.fuel_gal = 0

    def add_fuel(self, amount):
        self.fuel_gal += amount

    def drive(self, distance):
        required_fuel = distance / self.mpg
        if self.fuel_gal < required_fuel:
            print('Not enough gas.')
        else:
            self.fuel_gal -= required_fuel
            print('%f gallons remaining.' % self.fuel_gal)

class MotorCycle(MotorVehicle):
    def __init__(self, name, speed, mpg):
        MotorVehicle.__init__(self, name, speed, mpg)

    def wheelie(self):
        print('That is too dangerous.')


scooter = MotorCycle('Vespa', 55, 40)
dirtbike = MotorCycle('KX450F', 80, 25)

scooter.info()
dirtbike.info()
choice = input('Select scooter (s) or dirtbike (d): ')
bike = scooter if (choice == 's') else dirtbike

menu = '\nSelect add fuel(f), go(g), wheelie(w), quit(q): '
command = input(menu)
while command != 'q':
    if command == 'f':
        fuel = int(input('Enter amount: '))
        bike.add_fuel(fuel)
    elif command == 'g':
        distance = int(input('Enter distance: '))
        bike.drive(distance)
    elif command == 'w':
        bike.wheelie()
    elif command == 'q':
        break
    else:
        print('Invalid command.')

    command = input(menu)


## Unit testing
import unittest

# User-defined class
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14 * self.radius**2


# Class to test Circle
class TestCircle(unittest.TestCase):
    def test_compute_area(self):
        c = Circle(0)
        self.assertEqual(c.compute_area(), 0.0)

        c = Circle(5)
        self.assertEqual(c.compute_area(), 78.5)

    def test_will_fail(self):
        c = Circle(5)
        self.assertLess(c.compute_area(), 0)


if __name__ == "__main__":
    unittest.main()


#Assertion methods.
''' Method	Checks that
    assertEqual(a, b)	a == b
    assertNotEqual(a,b)	a != b
    assertTrue(x)	bool(x) is True
    assertFalse(x)	bool(x) is False
    assertIs(a, b)	a is b
    assertIsNot(a,b)	a is not b
    assertIsNone(x)	x is None   
    assertIsNotNone(x)	x is not None
    assertIn(a, b)	a in b
    assertNotIn(a, b)	a not in b
    assertAlmostEqual(a, b)	round(a - b, 7) == 0
    assertGreater(a, b)	a > b
    assertGreaterEqual(a, b)	a >= b
    assertLess(a, b)	a < b
    assertLessEqual(a, b)	a <= b
'''


# Pre-initialized arrays.
import numpy as np

zero_array = np.zeros((1, 5))   # Single dimension array with 5 elements
print('zero_array:')
print(zero_array)
print()

one_array = np.ones((5, 2))  # 5-dimension array with 2 elements in each dimension.
print('one_array:')
print(one_array)

'''
A common operation is to create a sequence of numbers, like 0, 1, 2, ... using range(). 
However, range() creates sequences of integers only and can not generate fractional values. 
The linspace numpy function creates a sequence by segmenting a given range with a specified number of points. 
For example, linspace(0, 1, 11) creates a sequence with 11 elements between 0 and 1: 0, 0.1, 0.2, ..., 0.9, 1.0.

Creating sequences using linspace().
'''
import numpy as np

print(np.linspace(0, 1, 11))
print()
print(np.linspace(0, np.sin(np.pi/4), 20))

'''
[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1. ]

[ 0.          0.03721615  0.07443229  0.11164844  0.14886459  0.18608073
  0.22329688  0.26051302  0.29772917  0.33494532  0.37216146  0.40937761
  0.44659376  0.4838099   0.52102605  0.5582422   0.59545834  0.63267449
  0.66989063  0.70710678]'''

'''
Table 16.15.1: Some commonly used Python standard library modules.
desired
Module name	        Description	            
datetime	        Creation and editing of dates and times objects
random	            Functions for working with random numbers	
copy	            Create complete copies of objects	
time	            Get the current time, convert time zones, sleep for a number of seconds	
math	            Mathematical functions	
os	                Operating system informational and management helpers	
sys	                System specific environment or configuration helpers	
pdb	                The Python interactive debugger	
urllib	            URL handling functions, such as requesting web pages	
'''

'''The random module is used to implement a simple game where a user continues to draw from a deck of cards 
until an ace card is found.'''
import random

# Create a shuffled card deck with 4 suites of cards 2-10, and face cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)

num_drawn = 0
game_over = False
user_input = input("Press any key to draw a card ('q' to quit): ")
while user_input != 'q' and not game_over:

    # Draw a random card, and remove card from the deck
    card = random.choice(deck)
    deck.remove(card)
    num_drawn += 1

    print('\nCard drawn:', card)

    # Game is over if an ace was drawn
    if card == 'A':
        game_over = True
    else:
        user_input = input("Press any key to draw a card ('q' to quit): ")

if user_input == 'q':
    print("\nGame was quit")
else:
    print(num_drawn, 'card(s) drawn to find an ace.')