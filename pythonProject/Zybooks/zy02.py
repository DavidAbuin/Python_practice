'''
x = 2 + 2
print (type(x))
print(type('ABC'))
print(id(x))
print(id('ABC'))
print()

#Floating-point Scientific Notation - Energy to mass conversion
c_meters_per_sec = 299792458  # Speed of light (m/s)
joules_per_AA_battery = 4320.5  # Nickel-Cadmium AA batteries
joules_per_TNT_ton = 4.184e9

#Read in a floating-point number from the user
mass_kg = float(input('Enter the mass kg: '))

#Compute E = mc2.
energy_joules = mass_kg * (c_meters_per_sec**2)  # E = mc^2
print('Total energy released:', energy_joules, 'Joules')

#Calculate equivalent number of AA and tons of TNT.
num_AA_batteries = energy_joules / joules_per_AA_battery
num_TNT_tons = energy_joules / joules_per_TNT_ton

print('Which is as much energy as:')
print('  ', num_AA_batteries, 'AA batteries')
print('  ', num_TNT_tons, 'tons of TNT')


minutes = int(input('Enter minutes:\n'))
hours = minutes // 60
minutes_remaining = minutes % 60

print(minutes, 'minutes is', end=' ')
print(hours, 'hours and', end=' ')
print(minutes_remaining, 'minutes.\n', end=' ')

phone_num = 9365551212
tmp_val = phone_num // 10000  # // 10000 shifts right by 4, so 936555.
prefix_num = tmp_val % 1000 # % 1000 gets the right 3 digits, so 555.

amount_to_change = 19
num_fives = amount_to_change // 5

num_ones = amount_to_change - num_fives % 5
print('Change for $', amount_to_change)
print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')

'''
my_string = 'This is a \n \'normal\' string\n'
my_raw_string = r'This is a \n \'raw\' string'

print(my_string)
print(my_raw_string)

ord('A') # returns 65
chr(90) # Between 0-255 returns ASCII char: z