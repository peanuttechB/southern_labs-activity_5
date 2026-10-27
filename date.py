# Author : Peanut


# Check if the year is a leap year.

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return Faelse
    if year % 4 == 0:
        return True
# All other years are not leap years
    return False
    

# Calculate the day of the week for a given date

def get_day_of_the_week(month, day, year):

    last_two_digits = year % 100
    twelves = last_two_digits // 12
    remainder = last_two_digits % 12
    fours = remainder // 4


    # Assign a month code based on the month

    if month == 1:
        month_code = 1
    elif month == 2:
        month_code = 4
    elif month == 3:
        month_code = 4
    elif month == 4:
        month_code = 0
    elif month == 5:
        month_code = 2
    elif month == 6:
        month_code = 5
    elif month == 7:
        month_code = 0
    elif month == 8:
        month_code = 3
    elif month == 9:
        month_code = 6
    elif month == 10:
        month_code = 1
    elif month == 11:
        month_code = 4
    else:
        month_code = 6


    # Start with no special offset
    special_offset = 0

    # Check the century and assign its offset
    if year >= 1600 and year < 1700:
        special_offset = 6
    elif year >= 1700 and year < 1800:
        special_offset = 4
    elif year >= 1800 and year < 1900:
        special_offset = 2
    elif year >= 1900 and year < 2000:
        special_offset = 0
    elif year >= 2000 and year < 2100:
        special_offset = 6
    elif year >= 2100 and year < 2200:
        special_offset = 4

    # Adjust January and February in leap years
    if (month == 1 or month == 2) and is_leap_year(year):
        special_offset = special_offset + 6

    # Add all the numbers together
    total = twelves + remainder + fours + day + month_code + special_offset
    day_number = total % 7

    # Return the name of day
    if day_number == 0:
        return "Saturday"
    elif day_number == 1:
        return "Sunday"
    elif day_number == 2:
        return "Monday"
    elif day_number == 3:
        return "Tuesday"
    elif day_number == 4:
        return "Wednesday"
    elif day_number == 5:
        return "Thursday"
    else:
        return "Friday"

# Test the function with different dates
def main():
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))


# Run the main function
main()





