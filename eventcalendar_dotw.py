"""
Set of functions for handling day of the week
"""


def is_leap_year(year):
    """This function will take a year and check whether it is a leap year and
    return True if so, and False if not."""
    if (int(year) % 4 == 0) and (int(year) % 100 != 0):
        return True
    elif int(year) % 400 == 0:
        return True
    else:
        return False


dotw_index = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}


def get_doomsday_dotw(year):
    """This function will take a integer year and return the day of the week index for the
    doomsday of that year."""
    # Find the doomsday for the first year in that century
    century = year - (year % 100)
    cent_dotw = century % 400

    # find dotw index for century
    if cent_dotw == 0:
        cent_index = 2
    elif cent_dotw == 100:
        cent_index = 0
    elif cent_dotw == 200:
        cent_index = 5
    elif cent_dotw == 300:
        cent_index = 3

    # find the number of times year (w/o centuries can be divided by 12
    div_12_index = (year - century) // 12
    # find the number of times the remainder can be divided by 4
    remainder_index = (year - century) % 12
    div_4_index = remainder_index // 4

    # Calculate dotw index for that year
    year_dotw_index = (cent_index + div_12_index + remainder_index + div_4_index) % 7

    return year_dotw_index


def get_dotw(date):
    """This function takes a date tuple and returns a day of the week index
    for that date, based on the doomsday day of the week. This function will call the
    get_doomsday_dotw() and is_leap_year functions."""

    # set month, day, year as variables
    target_month = int(date[0])
    target_day = int(date[1])
    target_year = int(date[2])

    # calculate the doomsday date for the given month
    if target_month == 1:
        if is_leap_year(target_year):
            dooms_day = 4
        else:
            dooms_day = 3

    elif target_month == 2:
        if is_leap_year(target_year):
            dooms_day = 29
        else:
            dooms_day = 28

    elif target_month == 3:
        dooms_day = 14

    elif target_month == 4:
        dooms_day = 4

    elif target_month == 5:
        dooms_day = 9

    elif target_month == 6:
        dooms_day = 6

    elif target_month == 7:
        dooms_day = 11

    elif target_month == 8:
        dooms_day = 8

    elif target_month == 9:
        dooms_day = 5

    elif target_month == 10:
        dooms_day = 10

    elif target_month == 11:
        dooms_day = 7

    elif target_month == 12:
        dooms_day = 12

    # calulate doomsday dotw
    dooms_dotw = get_doomsday_dotw(target_year)

    # calculate target day of the week
    target_dotw_index = ((target_day - dooms_day) + dooms_dotw) % 7

    return target_dotw_index
