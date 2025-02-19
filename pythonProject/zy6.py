nose = '0'  # Looks a little like a nose
user_value = '-'

#while user_value != 'q':
  #  print(' %s %s ' % (user_value, user_value))  # Print eyes
  #  print('  %s  ' % nose)  # Print nose
  #  print(user_value*5)  # Print mouth
 #   print('\n')

    # Get new character for eyes and mouth
 #   user_input = input("Enter a character ('q' for quit): ")
  #  user_value = user_input[0]

print('Goodbye.\n')

year_considered = 2025  # Year being considered
num_ancestors = 4  # Approx. ancestors in considered year
years_per_generation = 50  # Approx. years per generation

print(('Enter a past year (neg. for BCE):'))
user_year = 1880
print()


# While loops that count iterations: Saving Interest program
while year_considered >= user_year:
    print('Ancestors in %d: %d' % (year_considered, num_ancestors))

    num_ancestors = num_ancestors * 2
    year_considered = year_considered - years_per_generation

'''Program that calculates savings and interest'''

initial_savings = 100000
interest_rate = 0.13

print('Initial savings of $%d' % initial_savings)
print('at %d%% yearly interest.\n' % (interest_rate*100))

years = 10
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')

print()
# Iterating over a list using a for loop.
for name in ['Bill', 'Nicole', 'John']:
    print ('Hi %s!' % name)


print()
# A for loop assigns a dictionary's skeys to the loop variable.
channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 5,
    'NBC': 4,
    'CBS': 12
}

for c in channels:
    print('%s is on channel %d' % (c, channels[c]))

print()
# Using a for loop to access each character of a string
my_str = ''
for character in "Take me to the moon.":
    my_str += character + '_'
print(my_str)

daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75   # Sunday
]

total = 0
for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print('Weekly revenue: $%f' % total)
print('Daily average revenue: $%f' % average)

# Looping over a sequence in reverse
names = [
    'Thorin', 'Dwalin','Balin',
    'Kili', 'Fili',
    'Dori','Nori', 'Ori',
    'Oin','Gloin',
    'Bifur', 'Bofur', 'Bombur'
]

for name in names:
    print(name, '|', end=' ')

print('\nPrinting in reverse:')
for name in reversed(names):
    print(name, '|', end=' ')


# Using range()
'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

years = 6
print()

savings = initial_savings
for i in range(years):
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate)

print('\n')

print()
# Nested loops
'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
#while letter1 <= 'z':  # Outer loop
  #  letter2 = 'a'
 #   while letter2 <= 'z':  # Inner loop
 #       print('%s%s.com' % (letter1, letter2))
 #       letter2 = chr(ord(letter2) + 1)
#    letter1 = chr(ord(letter1) + 1)


num_rows =2
num_cols = 3

for i in range(num_rows):
    print(i, end =' ')
    for j in range(num_cols -1):
        i*=j
        print('*', end=' ')
    print('')


# Break statements
empanada_cost = 3
taco_cost = 4
'''
user_money = int(input('Enter money for meal: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print('$%d buys %d empanadas and %d tacos without change.' %
        (meal_cost, num_empanadas, num_tacos))
else:
    print('You cannot buy a meal without having change left over.')


# Continue Statement
empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

num_diners = int(input('How many people are eating: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
num_options = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):

        # Total items purchased must be equally divisible by number of diners
        if (num_tacos + num_empanadas) % num_diners != 0:
            continue

        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        if meal_cost == user_money:
            print('$%d buys %d empanadas and %d tacos without change.' %
                  (meal_cost, num_empanadas, num_tacos))
            num_options += 1

if num_options == 0:
    print('You cannot buy a meal without having change left over.')
'''

user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern = 'RRGBBRYBGY'

for i in range(len(simon_pattern)):
    x = simon_pattern[i]
    y = user_pattern[i]
    if x == y:
        user_score += 1
    else:
        break

print('User score:', user_score)

print()

import edit_distance

#A few legal, acceptable Danish names
legal_names = ['Thor', 'Bjork', 'Bailey', 'Anders', 'Bent', 'Bjarne', 'Bjorn',
    'Claus', 'Emil', 'Finn', 'Jakob', 'Karen', 'Julie', 'Johanne', 'Anna', 'Anne',
    'Bente', 'Eva', 'Helene', 'Ida', 'Inge', 'Susanne', 'Sofie', 'Rikkie', 'Pia',
    'Torben', 'Soren', 'Rune', 'Rasmus', 'Per', 'Michael', 'Mads', 'Hanne',
    'Dorte'
]

print(('Enter desired name:\n'))
user_name = 'Runa'
if user_name in legal_names:
    print('{} is an acceptable Danish name. Congratulations.'.format(user_name))
else:
    print('{} is not acceptable.'.format(user_name))
    for name in legal_names:
        if edit_distance.distance(name, user_name)  < 2:
            print('You might consider: {},'.format(name), end=' ')
            break
    else:
        print('No close matches were found.')
print('Goodbye.')

print()
#  Using range() and len() to iterate over a sequence.
origins = [4, 8, 10]

for index in range(len(origins)):
    value = origins[index]  # Retrieve value of element in list.
    print('Element %d: %s' % (index, value))

print()

# Using list.index() to find the index of each element.
for value in origins:
    index = origins.index(value)  # Retrieve index of value in list
    print('Element %d: %s' % (index, value))
print()
# The enumerate() function.
# The enumerate() function retrieves both the index and corresponding element value at the same time,
# providing a cleaner and more readable solution:
for (index, value) in enumerate(origins):
    print('Element %d: %s' % (index, value))

print()

# Dice statistics
# The following program calculates the number of times the sum of two dice (randomly rolled) is equal to six or seven.
import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid number of rolls. Try again.')
