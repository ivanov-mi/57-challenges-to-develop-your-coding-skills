from datetime import datetime

current_age = int(input("What is your current age? "))
retire_age = int(input("At what age would you like to retire? "))

current_year = datetime.now().year

years_left = retire_age - current_age
retirement_age = current_year + years_left

print("You have {} years left until you can retire.\nIt's 2015, so you can retire in {}.".format(years_left, retirement_age))