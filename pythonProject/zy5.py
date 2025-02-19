user_choice = 2  # Hardcoded values for this tool. Could be input()...
num_items = 5

if user_choice == 1:
    print('user_choice is 1')
elif user_choice == 2:
    if num_items < 0:
        print('user_choice is 2 and num_items < 0')
    else:
        print('user_choice is 2 and num_items >= 0')
else:
    print('user_choice is neither 1 or 2')

# Creating a Boolean
my_bool = True   # Assigns the boolean value True to my_bool

my_val  = 5
is_small = my_val < 3 # Evaluates the expression and assigns False to is_small
print(is_small)

young = True
famous = False

if (young and famous):
    print("You must be rich!")
else:
    print("There is always the lottery...")
print()
prices = ['$20', 14.99, 5]
print(14.99 in prices)

print()
#Checking for substrings
request_str = 'GET index.html HTTP/1.1'

if '/1.1' in request_str:
    print('HTTP protocol 1.1')

if 'HTTPS' not in request_str:
    print('Unsecured connection')

#Checking membership in a dict.
my_dict = {'A': 1, 'B': 2, 'C': 3}

if 'B' in my_dict:
    print("Found 'B'")
else:
   print("'B' not found")

# Membership operator does not check values
if 3 in my_dict:
    print('Found 3')
else:
    print('3 not found')
print()


# Identity operators
x = int(500 + 500) +0  # Create a new object with value 1000
y = int(500 + 500) + 0# Create a second object with value 1000
z = x  # Bind z to the same object as x

if z is x:
    print('z and x are bound to the same object,')
if z is not y:
    print('but z and y are not.')

print(id(z))
print(id(y))