# 33birthday.py by Gennie Fae Briones

# write a program that simulates the bday paradox by filling up classrooms of students with random chosen bdays
# make the number of days in the calendar and the number of ppl in the classroom command line arguments

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared = 0

for t in range(trials):
    students = [] # empty list of students
    for i in range(people):
        bday = random.randint(0, days-1)
        if bday in students:
            shared += 1
            break 
        students.append(bday)
print(shared/trials)