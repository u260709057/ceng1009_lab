SUNDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6

starting_day =float(input("enter the starting day:"))
ending_day = float(input("enter the ending day:"))
total_days = (ending_day - starting_day)
ending_day = total_days % 7
print("Your vacation ends on the day" , ending_day)