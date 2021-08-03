# App that calculates your age based on the birthday
import datetime
from datetime import date


def calculate_age(born):
    """Method to calculate the age based on the birthday"""
    today = date.today()
    # we compare 2 tuples and if True it will substract 1, else it will substract 0
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    if born.year > today.year:
        print("Wow, you are from the future :)")
    elif age == 0:
        print(f"You are so young, only {born.month - today.month - (born.day > today.day)} months old")
    elif age > 100:
        print(f"Nicely done! You have discovered the secret, you are {age} years old")
    else:
        print(f"You are {age} years old")


correct_date = True
while correct_date:
    try:
        birth_year = int(input("Please insert your birth year -> "))
        birth_month = int(input("Please insert your birth month -> "))
        birth_day = int(input("Please insert your birth day -> "))
        birthdate = datetime.date(year=birth_year, month=birth_month, day=birth_day)
    except ValueError:
        print("Incorrect date")
        correct_date = False
    else:
        calculate_age(birthdate)
        break

