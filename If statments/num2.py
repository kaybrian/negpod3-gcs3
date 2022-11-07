#!/usr/bin/python3
from calendar import monthrange
import datetime

now = datetime.datetime.now()
months = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12
}

Month_name = input("Input: ")
month_lower = Month_name.lower().strip()

try:
    if month_lower == 'february':
        num_days = "28 or 29 "
    else:
        num_days = monthrange(now.year, months[month_lower])[1]

    print(f"output:  The month of {Month_name} has {num_days} days")

except:
    print("Sorry, the Month you entered doesn't Exist")

