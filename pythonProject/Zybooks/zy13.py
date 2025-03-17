''' Exception Handling'''

user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except:
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")


# Multiple Exception types
user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except ValueError:
        print('Could not calculate health info.\n')
    except ZeroDivisionError:
        print('Invalid height entered. Must be > 0.')

    user_input = input("Enter any key ('q' to quit): ")

'''
try:
    # ...
except (ValueError, TypeError):
    # Exception handler for any ValueError or TypeError that occurs.
except (NameError, AttributeError):
    # A different handler for NameError and AttributeError exceptions.
except:
    # A different handler for any other exception type.
'''

# BMI example with error - checking code but without using exception-handling constructs.
user_input = ''
while user_input != 'q':
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        print('Invalid weight.')
    else:
        height = int(input('Enter height (in inches): '))
        if height <= 0:
            print('Invalid height')

    if (weight < 0) or (height <= 0):
        print('Can not compute info.')
    else:
        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov

    user_input = input("Enter any key ('q' to quit): ")

# BMI example with error-checking code that raises exceptions.
user_input = ''
while user_input != 'q':
    try:
        weight = int(input('Enter weight (in pounds): '))
        if weight < 0:
            raise ValueError('Invalid weight.')

        height = int(input('Enter height (in inches): '))
        if height <= 0:
            raise ValueError('Invalid height.')

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")

# BMI example using exception-handling constructs along with functions.
def get_weight():
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        raise ValueError('Invalid weight.')
    return weight

def get_height():
    height = int(input('Enter height (in inches): '))
    if height <= 0:
        raise ValueError('Invalid height.')
    return height

user_input = ''
while user_input != 'q':
    try:
        weight = get_weight()
        height = get_height()

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')

    user_input = input('Enter any key (\'q\' to quit): ')


# finally for cleaning up
def divide(a, b):
    z = -1
    try:
        z = a / b
    except ZeroDivisionError:
        print('Can not divide by zero')
    finally:
        print('Result is', z)