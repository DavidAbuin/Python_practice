# Modifying a list
short_names = ['Gertrude', 'Sam', 'Ann', 'Joseph']

del short_names[0]
short_names[-1] = 'Joe'

print(short_names)

short_names = ['Jan', 'Sam', 'Ann', 'Joe', 'Tod']

short_names.sort()
short_names.reverse()

print(short_names)

'''Iterating through a list example'''
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers:')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()  # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    print('%d: %d' % (index, value))

# Determine maximum even number
max_num = None
for num in nums:
    if (max_num == None) and (num % 2 == 0):
        # First even number found
        max_num = num
    elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
        # Larger even number found
        max_num = num

print('Max even #:', max_num)

# Using a variable to keep track of a value while iterating over a list.
nums = [1, 4, 15, 456]

max_even = None
for num in nums:
    if num % 2 == 0: # The number is even?
        if max_even == None or num > max_even:  # Greatest even number seen?
            max_even = num


#Finding the sum in a list of elements
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers: ')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    print('%d: %s' % (pos, token))

sum = 0
for num in nums:
    sum += num

print('Sum:', sum)

#Write a loop to populate user_guesses with num_guesses integers. Read integers using int(input()).
# Ex: If num_guesses is 3 and user enters 9 5 2, then user_guesses is [9, 5, 2].
num_guesses = 3
user_guesses = []

guess = 1
while guess <= num_guesses:
    user_input = int(input())
    user_guesses.append(user_input)
    guess +=1

print(user_guesses)

# Assign sum_extra with the total extra credit received given list test_grades.
# Full credit is 100, so anything over 100 is extra credit.
# For the given program, sum_extra is 8 because 1 + 0 + 7 + 0 is 8.
test_grades = [101, 83, 107, 90]
sum_extra = -999 # Initialize 0 before your loop

sum_extra = 0
for grade in test_grades:
    if grade > 100:
        sum_extra += grade - 100

print('Sum extra:', sum_extra)

# Write a loop to print all elements in hourly_temperature. Separate elements with a -> surrounded by spaces. Sample output for the given program:
# 90 -> 92 -> 94 -> 95
# Note: 95 is followed by a space, then a newline.

hourly_temperature = [90, 92, 94, 95]

new_ht = []
new_hourly_temps = ""

for temp in hourly_temperature:
    new_ht.append(str(temp))
    new_hourly_temps = ' -> '.join(new_ht)
print(new_hourly_temps, end =' \n')


# Iterating over multi-dimensional lists
currency = [

        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
]

for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()

#  Iterating through multi-dimensional lists using enumerate().
currency = [
   [1, 5, 10 ],  # US Dollars
   [0.75, 3.77, 7.53],  #Euros
   [0.65, 3.25, 6.50]  # British pounds
]
for row_index, row in enumerate(currency):
   for column_index, item in enumerate(row):
       print('currency[%d][%d] is %.2f' % (row_index, column_index, item))

'''Output is:
currency[0][0] is 1.00
currency[0][1] is 5.00
currency[0][2] is 10.00
currency[1][0] is 0.75
currency[1][1] is 3.77
currency[1][2] is 7.53
currency[2][0] is 0.65
currency[2][1] is 3.25
currency[2][2] is 6.50
'''

#Modifying a list during iteration example.
my_list = [3.2, 5.0, 16.5, 12.25]

for i in range(len(my_list)):
    my_list[i] += 5

# list.sort() method example: Alphabetically sorting book titles.
books = []
prompt = 'Enter new book: '
user_input = input(prompt).strip()

while (user_input.lower() != 'exit'):
    books.append(user_input)
    user_input = input(prompt).strip()

books.sort()

print('\nAlphabetical order:')
for book in books:
    print(book)

#Using sorted() to create a new sorted list from an existing list without modifying the existing list.
numbers = [int(i) for i in input('Enter numbers: ').split()]

sorted_numbers = sorted(numbers)

print('\nOriginal numbers:', numbers)
print('Sorted numbers:', sorted_numbers)

# Matrix multiplication of 4x2 and 2x3 matrices.-----------------------------

m1_rows = 4
m1_cols = 2
m2_rows = m1_cols  # Must have same value
m2_cols = 3

m1 = [
    [3, 4],
    [2, 3],
    [1, 2],
    [0, 2]
]

m2 = [
    [5, 4, 4],
    [0, 2, 3]
]

m3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# m1 * m2 = m3
for i in range(m1_rows):  # for each row of m1
    for j in range(m2_cols):  # for each column of m2
        # Compute dot product
        dot_product = 0
        for k in range(m2_rows): #  for each row of m2
            dot_product += m1[i][k] * m2[k][j]

        m3[i][j] = dot_product

for i in range(m1_rows):
    for j in range(m2_cols):
        print('%2d' % m3[i][j], end=' ')
    print()  # Print single newline