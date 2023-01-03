import datetime
import os
import random




def enter_event(datetime):
    """Takes a datetime object as input and stores it in an external file to be read later"""
    with open("events.txt", "a") as events_file:
        events_file.write(str(datetime) + "\n")


def read_events():
    """Returns a tuple with the information in the datetime objects stored in the events.txt file"""
    events = []
    with open("events.txt", "r") as events_file:
        for line in events_file:
            # Parse the datetime object from the string representation
            event_datetime = datetime.datetime.strptime(line.strip(), "%Y-%m-%d %H:%M:%S")
            # Extract the information from the datetime object
            year = event_datetime.year
            month = event_datetime.month
            day = event_datetime.day
            hour = event_datetime.hour
            minute = event_datetime.minute
            second = event_datetime.second
            # Add the event information to the list of events
            events.append((year, month, day, hour, minute, second))
    # Return the list of events as a tuple
    return tuple(events)

def create_random_events():
    """Creates five random datetime events and inserts them using the enter_event function"""
    for i in range(5):
        # Generate a random datetime object
        year = random.randint(2000, 2030)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        datetimeobj = datetime.datetime(year, month, day, hour, minute, second)
        # Insert the event using the enter_event function
        enter_event(datetimeobj)

create_random_events()