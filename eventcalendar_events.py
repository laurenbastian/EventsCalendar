"""
Set of functions for handling events
"""


def read_events():
    """This function will read the events.csv file
    and return a list of event tuples of the form
    (month, day, event name)"""

    # open the file
    file = open("events.csv", "r")
    if file.mode == "r":
        # read the file and split into lines
        event_lines = file.read().splitlines()

        # create a list to hold event tuples
        event_list = []

        # for each line in the file, create an event tuple and add it to the list
        for eventline in event_lines:
            event = (eventline.split(","))

            event_month = int(event[0])
            event_day = int(event[1])
            event_name = str(event[2])

            event_tuple = (event_month, event_day, event_name)

            event_list.append(event_tuple)

        # close the file
        file.close()

        return event_list

    else:
        print("ERROR READING FILE")
        return None


def sort_events(event_list):
    """This sort function will use selection sort to take an events list and sort it
    in ascending calendar order. It will return the sorted list"""

    # sort the range of the list
    for i in range(len(event_list)):

        # find the smallest event
        small = i
        for j in range(i+1, len(event_list)):
            if event_list[small] > event_list[j]:
                small = j

        # swap the two events
        event_list[i], event_list[small] = event_list[small], event_list[i]

    return event_list


def merge(left, right):
    """This function will merge two sorted event lists and return a joined sorted list with
    elements from the given lists"""

    # create joined_list and indices for left and right
    joined_list = []
    l_idx = 0
    r_idx = 0

    # combine the two lists
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            joined_list.append(left[l_idx])
            l_idx = l_idx + 1
        else:
            joined_list.append(right[r_idx])
            r_idx = r_idx + 1

    # append the remaining events in the list
    while l_idx < len(left):
        joined_list.append(left[l_idx])
        l_idx = l_idx + 1
    while r_idx < len(right):
        joined_list.append(right[r_idx])
        r_idx = r_idx + 1

    # return joined_list
    return joined_list


def sort_events_fast(event_list):
    """This sort function will use merge sort to take an events list and sort it
    in ascending calendar order. It will call the merge() function and itself, recursively.
    It will return the given list."""

    # BASE: a list of size 1 is always sorted
    if len(event_list) == 1:
        return event_list

    # divide the list into smaller lists
    mid = len(event_list) // 2
    left_list = event_list[:mid]
    right_list = event_list[mid:]

    # recursion to break into many lists of size 1
    left_list = sort_events_fast(left_list)
    right_list = sort_events_fast(right_list)

    # return the merged list
    return merge(left_list, right_list)


def is_same(date_1, date_2):
    """This function checks if the dates are the same.
        If so, return True, else return False"""
    if (date_1[0], date_1[1]) == (date_2[0], date_2[1]):
        return True
    else:
        return False


def is_before(date_1, date_2):
    """This function checks if date1 is before date2.
    If so, return True, else return False"""
    if (date_1[0], date_1[1]) < (date_2[0], date_2[1]):
        return True
    else:
        return False


def is_after(date_1, date_2):
    """This function checks if date1 is after date 2.
        If so, return True, else return False"""
    if (date_1[0], date_1[1]) > (date_2[0], date_2[1]):
        return True
    else:
        return False


def get_events_binary_search(date):
    """This function will utilize binary search methods to find events
    with a given target date. It will call read_events(), sort_events_fast(),
    is_before(), and is_after().
    It will return a list of events with the target date."""

    # create a list of target events
    target_events = []

    # read and sort the event list
    events_list = sort_events_fast(read_events())

    # Set true to get into the while loop
    more_events = True

    while more_events:
        # assume that there are no more events until we add an event to the list
        more_events = False

        # create indices
        low = 0
        high = len(events_list) - 1

        # conduct a binary search of the events list
        while low <= high:
            mid = (low + high) // 2
            if is_after(date, events_list[mid]):
                low = mid + 1
            elif is_before(date, events_list[mid]):
                high = mid - 1
            elif is_same(date, events_list[mid]):
                # add the event name to the target events list and remove from full event list
                target_events.append(events_list[mid][2])
                events_list.pop(mid)
                # check for more events and break current loop
                more_events = True
                break
    # return a list of the events on the given date
    return target_events
