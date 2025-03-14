'''Dictionaries'''

# Delete from a Dictionary
country_capital = {'Spain': 'Madrid', 'Togo': 'Lome', 'Prussia': 'Konigsberg'}

del country_capital['Prussia']

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')

# Iterating over a dict.
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda, calories in num_calories.items():
    print('%s: %d' % (soda, calories))
print()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.keys():
    print(soda)
print()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.values():
    print(soda)

print()

# Use list() to convert view objects into lists.
solar_distances = dict(mars=219.7e6, venus=116.4e6, jupiter=546e6, pluto=2.95e9)
list_of_distances = list(solar_distances.values())  # Convert view to list

closest = sorted(list_of_distances)[0]
next_closest = sorted(list_of_distances)[1]

print('Closest planet is %.4e' % closest)
print('Second closest planet is %.4e' % next_closest)

country_pop = {
    'China':         1365830000,
    'India':         1247220000,
    'United States': 318463000,
    'Indonesia':     252164800
} # country populations as of 2014

for items in country_pop.items():
    country = items[0]
    pop = items[1]

    print(country, 'has', pop, 'people.')


# Nested dictionaries
# Nested dictionaries example: Storing grades.
grades = {
    'John Ponting': {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = input('Enter student name: ')

while user_input != 'exit':
    if user_input in grades:
        # Get values from nested dict
        homeworks = grades[user_input]['Homeworks']
        midterm = grades[user_input]['Midterm']
        final = grades[user_input]['Final']

        # print info
        for hw, score in enumerate(homeworks):
            print('Homework {}: {}'.format(hw, score))

        print('Midterm: {}'.format(midterm))
        print('Final: {}'.format(final))

        # Compute student total score
        total_points = sum([i for i in homeworks]) + midterm + final
        print('Final percentage: {:.1f}%'.format(100*(total_points / 500.0)))

    user_input = input('Enter student name: ')

'''Output:
Enter student name: Ricky Bobby
Homework 0: 50
Homework 1: 52
Homework 2: 78
Midterm: 40
Final: 65
Final percentage: 57.0%
...
Enter student name: John Ponting
Homework 0: 79
Homework 1: 80
Homework 2: 74
Midterm: 85
Final: 92
Final percentage: 82.0%
'''