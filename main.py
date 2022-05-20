
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ' '
    month = ' '
    day = ' '
    while city != 'Chicago' and city != 'New York City' and city != 'Washington':
        city = input("\nenter city\n").title()

    while month != 'All' and month != 'January' and month != 'February' and month != 'March' and month != 'April ' and month != 'May' and month != 'Jwune':
        month = input("\nenter month\n").title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("\nenter day\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'All':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('most common month=', most_common_month)
    print('most common day', most_common_day)
    print('most common hour', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # TO DO: display most commonly used start station
    most_common_ss = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    most_common_es = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip

    most_common_cs=df.groupby(['Start Station', 'End Station']).size().nlargest(1)


    print('most common start station', most_common_ss)
    print('most common end station', most_common_es)
    print('Most Common combination of start station and end station ',most_common_cs)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_time = df['Trip Duration'].sum()/(60*60*24)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()/60

    print('total time in days', round(total_time))
    print('mean time in mins', round(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    types = df['User Type'].value_counts()

    print('User Types:\n', types)

    # TO DO: Display counts of gender

    try:
      gender = df['Gender'].value_counts()
      print('\nGender Types:\n', gender)
    except KeyError:
      print("Gender,No data ")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      oldest = int(df['Birth Year'].min())
      print('\nEarliest Year:', oldest)
    except KeyError:
      print(" Earliest Year No data .")

    try:
      youngest = int(df['Birth Year'].max())
      print('\nMost Recent Year:', youngest)
    except KeyError:
      print('Most Recent Year:No data')

    try:
      most_common_year = int( df['Birth Year'].mode()[0])
      print('\nMost Common Year:', most_common_year)
    except KeyError:
      print("Most Common Year:No data ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    req = input('\ndo you want to display 5 rows of data ? Enter yes or no\n').lower()
    i = 0
    pd.set_option('display.max_columns',200)

    while True:
        if req == 'yes':
            print(df.iloc[i:i + 5])
            i=i+5

            req = input('\ndo you want to display next 5 rows of data ? Enter yes or no\n').lower()
        elif req == 'no':
            break
        else:
            req = input('\ndo you want to display next 5 rows of data ? Enter yes or no\n').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()