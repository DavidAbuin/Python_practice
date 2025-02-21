george_v = "His Majesty George V, by the Grace of God, " \
           "of the United Kingdom of Great Britain and " \
           "Ireland and of the British Dominions beyond " \
           "the Seas, King, Defender of the Faith, Emperor of India"
gandhi = 'Mohandas Karamchand Gandhi'
john_f_kennedy = 'JFK'

print(len(george_v), 'characters is much too long of a name!')
print(len(gandhi), 'characters is better...')
print(len(john_f_kennedy), 'characters is short enough.')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[0], alphabet[1], alphabet[25])

#List BASICS

# Some of the most expensive cars in the world
lamborghini_veneno = 3900000  # $3.9 million!
bugatti_veyron = 2400000      # $2.4 million!
aston_martin_one77 = 1850000  # $1.85 million!

prices = [lamborghini_veneno, bugatti_veyron, aston_martin_one77]

print('Lamborghini Veneno:', prices[0], 'dollars')
print('Bugatti Veyron Super Sport:', prices[1], 'dollars')
print('Aston Martin One-77:', prices[2], 'dollars')

# Adding and removing list elements.
my_list = [10, 'bw']
print (my_list)

my_list.append('abc')
print ('After append:', my_list)

my_list.pop(1)
print ('After pop:', my_list)

my_list.remove('abc')
print ('After remove:', my_list)

#Program to calculate statistics from student test scores.
midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]

#Combine the scores into a single list
all_scores = midterm_scores + final_scores

num_midterm_scores = len(midterm_scores)
num_final_scores = len(final_scores)

print(num_midterm_scores, 'students took the midterm.')
print(num_final_scores, 'students took the final.')

#Calculate the number of students that took the midterm but not the final
dropped_students = num_midterm_scores - num_final_scores
print(dropped_students, 'students must have dropped the class.')

lowest_final = min(final_scores)
highest_final = max(final_scores)

print('\nFinal scores ranged from', lowest_final, 'to', highest_final)

# Using tuples
white_house_coordinates = (38.8977, 77.0366)
print('Coordinates:', white_house_coordinates)
print('Tuple length:', len(white_house_coordinates))

# Access tuples via index
print('\nLatitude:', white_house_coordinates[0], 'north')
print('Longitude:', white_house_coordinates[1], 'west\n')

#Dictionary basics
players = {
    'Lionel Messi': 10,
    'Cristiano Ronaldo': 7
}

print(players)

caffeine_content_mg = {
    'Mr. Goodbar chocolate': 122,
    'Red Bull': 33,
    'Monster Hitman Sniper energy drink': 270,
    'Lipton Brisk iced tea - lemon flavor': 2,
    'dark chocolate coated coffee beans': 869,
    'Regular drip or percolated coffee': 60,
    'Buzz Bites Chocolate Chews': 1639
}

print(caffeine_content_mg)

#Adding, modifying, and removing dictionary entries
prices = {}  # Create empty dictionary
prices['banana'] = 1.49  # Add new entry
print(prices)

prices['banana'] = 1.69  # Modify entry
print(prices)

del prices['banana']  # Remove entry
print(prices)

#Conversion specifiers - using string formatting expressions
total_people = 75
dollars = 68
best_friend = 'Sydnie'

print('Your best friend is %s.' % best_friend)

print('You know %d people.' % total_people)

print('You have $%f dollars.' % dollars)

# %x, %X	Substitute as hexadecimal in lowercase (%x) or uppercase (%X).
# print('%x' % 31)
# %e, %E	Substitute as floating-point exponential format in lowercase (%e) or uppercase (%E).
# print('%E' % 15.2)
print('%x' % 31)
print('%E' % 15.2)

years = 15
total = 500 * (years * 0.02)
print('Savings after %d years is: %f' % (years, total))

# math module
import math

#base = float(input('Enter initial savings: '))
print()

#rate = float(input('Enter annual interest % rate: '))
print()

#years = int(input('Enter years that pass: '))
print()

#total = base * math.pow(1 + (rate / 100), years)

#print ('Savings after', years, 'years is', total)


num = 49
num_sqrt = math.sqrt(num)

x1 = 1.0
y1 = 2.0
x2 = 1.0
y2 = 5.0
point_dist = 0.0


point_dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print('Point distance:', point_dist)


