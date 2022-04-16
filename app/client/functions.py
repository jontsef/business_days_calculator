import pandas as pd
import datetime


def business_day_diff(start_dt, end_dt):
    if end_dt < start_dt:
        return -1
    calendar = pd.read_csv("calendar.csv")
    calendar['date'] = pd.to_datetime(calendar['date'])
    calender = calendar.loc[(calendar.date < end_dt) & (calendar.date > start_dt)]
    return sum(calender.business_day)


def calculate_due_date(start_dt, business_days):
    max_assumed_end = start_dt + datetime.timedelta(days=15 + business_days + (business_days//7)*2 + (business_days//250)*10)
    calendar = pd.read_csv("calendar.csv")
    calendar['date'] = pd.to_datetime(calendar['date'])
    calendar = calendar.loc[(calendar.date < max_assumed_end) & (calendar.date > start_dt)]
    current_bis_days = sum(calendar.business_day)
    while current_bis_days > business_days:
        calendar = calendar[:-1]
        current_bis_days = sum(calendar.business_day)
    return list(calendar['date'])[-1]


"""
# checks 
s = datetime.datetime(year=2022, month= 5, day=4)
e = datetime.datetime(year=2022, month= 5, day=9)

print(business_day_diff(start_dt = s, end_dt = e))
print(calculate_due_date(start_dt=s, business_days=4))
"""