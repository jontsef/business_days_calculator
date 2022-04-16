import pandas as pd
import datetime

url = "https://www.timeanddate.com/holidays/israel/"

# create a df with all holidays dates
holidays_df = pd.DataFrame({'holiday_date':[]})

for year in range(2022, 2031):
    # read the holidays table fro the website
    yearly_url = url + str(year)
    df = pd.read_html(url)[0]
    df.reset_index()
    df = df.astype('string')
    # rename columns
    df = df.set_axis(['date', 'day', 'name', 'type'], axis=1, inplace=False)
    # filter for only national holidays
    df = df.loc[df['type'].str.contains('National holiday', na=False)]
    # add the year
    df['date'] = df['date'] + " " + str(year)
    # read to a datetime format
    df['date'] = df['date'].apply(lambda x: datetime.datetime.strptime(x, "%b %d %Y"))
    df = df[['date']]
    # rename column
    df = df.set_axis(['holiday_date'], axis=1, inplace=False)
    # append to the main df
    holidays_df = holidays_df.append(df, ignore_index=True)


# create a df with all the dates in the range
df_all_dates = pd.DataFrame({'date': pd.date_range(start='16/04/2022', end='30/12/2030', freq='D')})


# join the df with the holidays dates and the df with all the dates in the time range
df = pd.merge(
    left=df_all_dates,
    right=holidays_df,
    how="left",
    on=None,
    left_on='date',
    right_on='holiday_date',
    left_index=False,
    right_index=False,
    sort=True,
    suffixes=("", ""),
    copy=True,
    indicator=False,
    validate=None,
)


def is_business_day(dt, holiday_date_column):
    if not pd.isnull(holiday_date_column):
        return 0
    elif dt.weekday() in [4,5]:
        return 0
    else:
        return 1


# create a business_day column
df['business_day'] = df.apply(lambda x: is_business_day(dt=x['date'], holiday_date_column=x['holiday_date']), axis=1)
# keep only the relevant columns
df = df[['date', 'business_day']]

# save to a csv
df.to_csv("calendar.csv")


