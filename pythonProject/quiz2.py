from random import *

date = randint(1, 30)
sundays = [7, 14, 21, 28]

if date in sundays:
    print("Try again,",date, "day is Sunday.")
else:
    print("The study date is ", date, "day of each month.")