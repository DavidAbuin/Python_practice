# Calling a recursive function
# Writing a statement that calls the recursive function backwards_alphabet() with starting_letter

def backwards_alphabet(curr_letter):
    if curr_letter == 'a':
        print (curr_letter)
    else:
        print(curr_letter)
        prev_letter = chr(ord(curr_letter) - 1)
        backwards_alphabet(prev_letter)

starting_letter = 'f'
backwards_alphabet(starting_letter)

# A recursive function find() carrying out a binary search algorithm

def find(low, high):
    mid = (high + low) // 2 # midpoint of low..high
    answer = input('Is it %d? (l/h/y): ' % mid)

    if (answer != 'l') and (answer != 'h'): # Base case
        print("Got it!")
    else:
        if answer == 'l':
            find(low,mid)
        else:
            find(mid+1, high)

print('Choose a number from 0 to 100.')
print('Answer with:')
print('   l (your num is lower)')
print('   h (your num is higher)')
print(' any other key (guess is right).')

find(0, 100)

# Recursive function for n factorial
def nfact(n):
    if n == 1 or n == 0:  # Base case
        fact = 1
    else:       # Recursive case
        fact = n * nfact(n-1)
    return fact

# Returns number of penniees if pennies are doubled num_days times
def double_pennies(num_pennies, num_days):
    total_pennies = 0

    if num_days == 0:
        total_pennies = num_pennies
    else:
        total_pennies = double_pennies((num_pennies * 2), (num_days-1))
    return total_pennies

#Program computes pennies if you have 1 penny today, 2 pennies after day 1, four pennies after 2 days, and so on.
starting_pennies = 1
user_days = 10

print('Number of pennies after', user_days, 'days: ', end="")
print(double_pennies(starting_pennies, user_days))


# Recursive function
def print_factorial(fact_counter, fact_value):
    output_string = ''

    if fact_counter == 0:
        output_string += '1'
    elif fact_counter == 1:
        output_string += str(fact_counter) + ' = ' + str(fact_value)
    else:
        output_string += str(fact_counter) + ' * '
        next_counter = fact_counter - 1
        next_value = next_counter * fact_value
        output_string += print_factorial (fact_counter -1, next_value)

    return output_string

user_val = 5
print('%d! = ' % user_val, end="")
print(print_factorial(user_val, user_val))

# Fibonacci sequence step-by-step
"""
Output the Fibonacci sequence step-by-step.
Fibonacci sequence starts as:
0 1 1 2 3 5 8 13 21 ... in which the first
two numbers are 0 and 1 and each additional
number is the sum of the previous two numbers
"""
def fibonacci(v1, v2, run_cnt):
    print(v1, '+', v2, '=', v1+v2)

    if run_cnt <= 1:  # Base case:
                      # Ran for user's number of steps
        pass  # Do nothing
    else:             # Recursive case
        fibonacci(v2, v1+v2, run_cnt-1)


print ('This program outputs the\n'
       'Fibonacci sequence step-by-step,\n'
       'starting after the first 0 and 1.\n')

run_for = int(input('How many steps would you like?'))

fibonacci(0, 1, run_for)

'''
The GCD is the largest number that divides evenly into two numbers, e.g. GCD(12, 8) = 4. 
A simple algorithm to compute the GCD subtracts the smaller number from the larger number until both numbers are equal. 
For example, GCD(12, 8) = GCD(12-8=4, 8) = GCD(4, 8-4=4). The equal numbers are the GCD. Euclid described this algorithm 
around 300 BC.

The below program recursively computes the GCD of two numbers. The base case is that the two numbers are equal, so that 
number is returned. The recursive case subtracts the smaller number from the larger number and then calls GCD with the 
new pair of numbers.
'''
# Calculate the greatest common divisor between two numbers
"""
Determine the greatest common divisor
of two numbers, e.g., GCD(8, 12) = 4
"""
def gcd(n1, n2):
    greatest_common_divisor = 0

    if n1 == n2:  # Base case: Numbers are equal
        greatest_common_divisor = n1
    else:  # Recursive case: Try again after subtracting
           # the smaller number from the larger number.
        if n1 > n2:  # n2 is smaller
            greatest_common_divisor = gcd(n1-n2, n2)
        else:        # n1 is smaller
            greatest_common_divisor = gcd(n1, n2-n1)
    return greatest_common_divisor

print ('This program outputs the greatest '
       'common divisor of two numbers.\n')

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

if (num1 < 1) or (num2 < 1):
    print('Note: Neither value can be below 1.')
else:
    my_gcd = gcd(num1, num2)
    print('Greatest common divisor =', my_gcd)


'''
Write code to complete raise_to_power(). Sample output if user_base is 4 and user_exponent is 2 is shown below. 
Note: This example is for practicing recursion; a non-recursive function, or using the built-in function math.pow(), 
would be more common.
4^2 = 16
'''
def raise_to_power(base_val, exponent_val):
   if exponent_val == 0:
      result_val = 1
   else:
      result_val = base_val *  raise_to_power(base_val, exponent_val-1)

   return result_val

user_base = 4
user_exponent = 2

print('%d^%d = %d' % (user_base, user_exponent,
      raise_to_power(user_base, user_exponent)))

# Finding distance of traveling to 3 cities
num_cities = 3
city_names = []
distances = []

def travel_paths(curr_path, need_to_visit):
    if len(curr_path) == num_cities:  # Base case: Visited all cities
        total_distance = 0
        for i in range(len(curr_path)):
            print(city_names[curr_path[i]], '  ', end=' ')

            if i > 0:
                total_distance += distances[curr_path[i-1]][curr_path[i]]

        print('=', total_distance)
    else:  # Recursive case: Travel to each city
        for i in range(len(need_to_visit)):
            # Visit city
            city = need_to_visit[i]
            need_to_visit.pop(i)
            curr_path.append(city)

            travel_paths(curr_path, need_to_visit)

            # Take item out of bag
            need_to_visit.insert(i, city)
            curr_path.pop()

distances.append([0])
distances[0].append(960)  # Boston-Chicago
distances[0].append(2960) # Boston-Los Angeles
distances.append([960])   # Chicago Boston

distances[1].append(0)
distances[1].append(2011) # Chicago-Los Angeles

distances.append([2960])  # Los Angeles-Boston
distances[2].append(2011) # Los Angeles-Chicago
distances[2].append(0)

city_names = ["Boston", "Chicago", "Los Angeles"]

path = []
need_to_visit = [0, 1, 2] # (Need to visit all 3 cities)
travel_paths(path, need_to_visit)