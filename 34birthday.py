#34birthday.py by Gennie Fae Briones

# same as 33birthday.py but make a list from the calendar

import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

shared = 0

for t in range(trials):
    calendar = [] #empty calendar
    for i in range(days):
        calendar.append(0)
    
    for i in range(students): # add bdays
        bday = random.randint(0, days-1)
        calendar[bday] += 1

    #check for shared bdays 
    shared_dates = []
    collision = False
    for day in range(len(calendar)):
        if calendar[day] > 1: 
            collision = True
    if collision: shared += 1

print(shared/trials)