import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New york city, or Washington?').lower()
        if city not in CITY_DATA:
            print("That is not a valid input. Try again!")
            continue   
        else:
            print("Well done!")
            break
    
    while True:
        time = input("Would you like to filter the data by month, day, both, or not filter?").lower()               

    # TO DO: get user input for month (all, january, february, ... , june)
        if time == 'month':
            month = input('Which month? January, February, March, April, May or June?').lower()
            day = 'all'
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        if time == 'day':
            day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?').lower()
            month = 'all'
            break
    # all
        if time == 'both':
            month = input('Which month? January, February, March, April, May or June?').lower()
            day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?').lower()
            break
            
    # not filter
        if time == 'not filter': 
            month = 'all'
            day = 'all'
            break
        else:
            print("That is not a valid input. Try again!")
            continue
            
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common month
    print ('The most common month:', df['month'].mode()[0])
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.hour
    print('The most common day:', df['day_of_week'].mode()[0])
    # TO DO: display the most common start hour
    print('The most common start hour:', df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station:', df['Start Station'].value_counts().head(1))

    # TO DO: display most commonly used end station
    print('Most commonly used end station:', df['End Station'].value_counts().head(1))

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip:\n', (df['Start Station'] +'     '+ df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Count of user types:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('Count of gender:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Earliest year of birth:', df['Birth Year'].min())
    print('Most recent year of birth:', df['Birth Year'].max())
    print('Most common year of birth:', df['Birth Year'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    # raw counter
    start_raw = 0
    end_raw = 5
    while True:
        x = input("Would you like to view any row data? Please input: Yes or No.  ").lower()
        # Check input value
        if x not in ['yes', 'no']:
            print("That is not a valid input. Try again!")
            continue
        if x == 'yes':
            print(df.iloc[start_raw : end_raw]) 
            # restart raw counter
            start_raw = start_raw + 5
            end_raw = end_raw + 5
            continue
        if x == 'no':
            break
    
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data (df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
