
# Using classes and attribute reference
class Time(object):
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def print_time(self):
        print('Hours:', self.hours, end=' ')
        print('Minutes:', self.minutes)

time1 = Time()
time1.hours = 7
time1.minutes = 15
time1.print_time()

class RaceTime:

    def __init__(self, start_hrs, start_mins, end_hrs, end_mins, dist):
        self.start_hrs = start_hrs
        self.start_mins = start_mins
        self.end_hrs = end_hrs
        self.end_mins = end_mins
        self.distance = dist

    def print_time(self):
        total_time = self._diff_time()
        print('Time to complete race: %d:%d' % (total_time[0], total_time[1]))

    def print_pace(self):
        total_time = self._diff_time()
        total_minutes = total_time[0] * 60 + total_time[1]
        print('Avg pace (mins/mile): %.2f' % (total_minutes / self.distance))

    def _diff_time(self):
        """Calculate total race time. Returns a 2-tuple (hours, minutes)"""
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        return (hours, minutes)

distance = 5.0

start_hrs = int(input('Enter starting time hours: '))
start_mins = int(input('Enter starting time minutes: '))
end_hrs = int(input('Enter ending time hours: '))
end_mins = int(input('Enter ending time minutes: '))

race_time = RaceTime(start_hrs, start_mins, end_hrs, end_mins, distance)

race_time.print_time()
race_time.print_pace()
print()
print()

class Employee:
    def __init__(self, name, wage=8.25, hours=20):
        """
        Default employee is part time (20 hours/week)
        and earns minimum wage
        """
        self.name = name
        self.wage = wage
        self.hours = hours



todd = Employee('Todd')  # Typical part-time employee
jason = Employee('Jason')  # Typical part-time employee
tricia = Employee('Tricia', wage=12.50, hours=40)  # Manager employee

employees = [todd, jason, tricia]

for e in employees:
    print ('%s earns %.2f per week' % (e.name, e.wage*e.hours))

print()
class Toy:
    def __init__(self, name, price, min_age):
        self.name = name
        self.price = price
        self.min_age = min_age

    def __str__(self):
        return ('%s costs only $%.2f. Not for children under %d!' %
                (self.name, self.price, self.min_age))

truck = Toy('Monster Truck XX', 14.99, 5)
print(truck)



# Define a custom exception type
class LessThanZeroError(Exception):
    def __init__(self, value):
        self.value = value

my_num = int(input('Enter number: '))

if my_num < 0:
    raise LessThanZeroError('my_num must be greater than 0')
else:
    print('my_num:', my_num)