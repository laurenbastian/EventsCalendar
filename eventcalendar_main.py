"""
Events Calendar:
This program prints a Sunday to Saturday calendar based on a user given date
between the years 1000 AD and 9999 AD

Lauren Bastian
"""

from eventcalendar_dotw import get_dotw, dotw_index, is_leap_year
from eventcalendar_events import get_events_binary_search

# A dictionary to store month names
month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def validate_input(date_string):
    """This function will take a string and check whether it is a valid date.
    If the input is valid, the function returns a date tuple in the form (month, day, year).
    If the input is invalid, the function returns None.
    A valid date will be in the form month-day-year where month (1-12), day (1-28/29/30/31) and
     year (1000 - any 4 digit year)."""

    # split the date into a list of chars
    date_list = (date_string.split("-"))

    # check if the list has 3 items
    # DO WE HAVE TO ACCOUNT FOR NON-NUMERIC INPUTS????
    if len(date_list) != 3:
        return None

    month = (date_list[0])
    day = (date_list[1])
    year = (date_list[2])

    # check if the components can be converted to integers
    if month.isdigit():
        month = int(date_list[0])
        day = int(date_list[1])
        year = int(date_list[2])
    else:
        return None

    # check that month is valid
    if (month < 1) or (month > 12):
        return None

    # check that that the year is valid
    if (year < 1000) or (year > 9999):
        return None

    # check whether days are valid
    # check whether it is february
    if month == 2:
        # check whether there is a leap year
        if is_leap_year(year):
            if (day < 1) or (day > 29):
                return None
        else:
            if (day < 1) or (day > 28):
                return None
    # check months with 31 days
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if (day < 1) or (day > 31):
            return None
    # check months with 30 days
    else:
        if (day < 1) or (day > 30):
            return None

    # if no invalid inputs, then return a date tuple (month, day, year)
    date_tuple = (month, day, year)
    return date_tuple


def next_date(date):
    """This function takes a date tuple and returns the date tuple of the next day."""
    # split tuple into day month and year for easy comparisons
    month = date[0]
    day = date[1]
    year = date[2]

    # check if it is December 31st
    if month == 12 and day == 31:
        return (1, 1, year + 1)

    # check if it is the 31st of month (not December)
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and (day == 31):
        return (month+1, 1, year)

    # check if it is the 30th of the month
    if (month == 4 or month == 6 or month == 9 or month == 11) and (day == 30):
        return (month+1, 1, year)

    # February Checks
    if month == 2:
        # check if it is last day of February
        if is_leap_year(year) and (day == 29):
            return (month+1, 1, year)
        elif not(is_leap_year(year)) and (day == 28):
            return (month+1, 1, year)
        # check if it is February 28th on a Leap Year
        elif is_leap_year(year) and (day == 28):
            return (month, day+1, year)
        # else return the next day of february
        else:
            return (month, day+1, year)
    # if no special cases are triggered, increase the day by 1 and return the date tuple
    else:
        return (month, day+1, year)


def previous_date(date):
    """This function takes a date tuple and returns the date tuple of the previous date"""
    # split tuple into day month and year for easy comparisons
    month = date[0]
    day = date[1]
    year = date[2]

    # check if it is the first of the month
    if day == 1:
        # check whether it is January first
        if month == 1:
            return (12, 31, year - 1)

        # check if it is March first
        if month == 3:
            if is_leap_year(year):
                return (2, 29, year)
            else:
                return (2, 28, year)

        # check if the previous month has 31 days
        if month-1 == 1 or month-1 == 3 or month-1 == 5 or month-1 == 7 or month-1 == 8 or month-1 == 10:
            return (month - 1, 31, year)

        # check if the previous month has 30 days
        if month-1 == 4 or month-1 == 6 or month-1 == 9 or month-1 == 11:
            return (month - 1, 30, year)

    # if no special cases are triggered, return date tuple as expected
    return (month, day - 1, year)


def find_sunday(date):
    """This function will take a given date and return the date tuple of the Sunday of the given week.
    This function will call itself recursively."""
    if get_dotw(date) == 0:
        return date
    else:
        return find_sunday(previous_date(date))


def print_calendar(date):
    """This function will take the target date print the weekly calendar from Sunday to Saturday
    It will make calls to find_sunday() and next_date()"""

    # create a date tuple for Sunday
    print_date = find_sunday(date)

    # print the weekly calendar
    for i in range(7):
        print(f"{dotw_index[get_dotw(print_date)]}, {month_names[int(print_date[0])]} {print_date[1]}")
        if len(get_events_binary_search(print_date)) == 0:
            print(" - No events")
        for event in get_events_binary_search(print_date):
            print(f" - {event}")
        print_date = next_date(print_date)


if __name__ == "__main__":
    """This is a program to print a Sunday - Saturday calendar
    of events based on a user entered date."""

    # prompt user for a date and validate
    my_date = input("Enter a date: ")
    my_date_tuple = validate_input(my_date)
    print()

    # print calendar
    print_calendar(my_date_tuple)
