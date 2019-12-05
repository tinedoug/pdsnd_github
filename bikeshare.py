#Some changes for a commit
import time
import pandas as pd
import numpy as np
from datetime import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']  
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] 

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
    cityname = input("Enter the city to analyze: ").lower()
    while cityname not in CITY_DATA.keys():
        print('This is not a valid city: ')
        cityname = input("Enter the city to analyze: ").lower
    else:
        city = cityname


        
    # TO DO: get user input for month (all, january, february, ... , june)
    monthinp = input("Enter the month to analyze: ").lower()
    while monthinp not in MONTH_DATA:
        print('This is not a valid month: ')
        monthinp = input("Enter the month to analyze: ").lower
    else:
        month = monthinp
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayinp = input("Enter the day to analyze: ").lower()
    while dayinp not in DAY_DATA:
        print('This is not a valid day: ')
        dayinp = input("Enter the day to analyze: ").lower
    else:
        day = dayinp
    

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
    df = pd.read_csv(CITY_DATA[city])
            
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day_name().str.lower()
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['start_hour'] = df['Start Time'].dt.hour
    if month != 'all':
        df = df.loc[df['month'] == month]
    if day != 'all':
        df = df.loc[df['day'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month is: ', df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print('Most common day of the week is: ', df['day'].value_counts().idxmax())


    # TO DO: display the most common start hour
    print('Most common start hour is: ', df['start_hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station is: ', df['Start Station'].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print('Most common end station is: ', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Stations'] = df['Start Station'] + ' and ' + df['End Station']
    
    print('Most common combined start and end station is: ', df['Combined Stations'].value_counts().idxmax())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(df.head())

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        dfUT = df.groupby('User Type').count()
        dfUT = dfUT[['Unnamed: 0']]
        dfUT = dfUT.rename(columns={'Unnamed: 0': 'Counts'})
        print(dfUT)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        dfG = df.groupby('Gender').count()
        dfG = dfG[['Unnamed: 0']]
        dfG = dfG.rename(columns={'Unnamed: 0': 'Counts'})
        print(dfG)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print ('The earliest birth year is: ', int(df['Birth Year'].min()))
        print ('The latest birth year is: ', int(df['Birth Year'].max()))
        print ('The most common birth year is: ', int(df['Birth Year'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_rows(df):
    
    sample = input("Would you like to view sample rows: ").lower()
    current_line = 0
    while sample == 'yes':
        current_slice_data = df.iloc[current_line:current_line + 5, :-3]
        print (current_slice_data.head(5))
        current_line = current_line + 5
        sample = input("Would you like to see more sample rows: ").lower
    else:
        sample == 'no'
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
