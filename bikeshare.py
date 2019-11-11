import time
import datetime
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("\nWould you like to see data for Chicago, New York, or Washington?\n").lower()
    while(True):
          if (city in CITY_DATA.keys()):
            break
        else:
            city = input('Enter Correct city: ').lower()


    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month wold you like to filter by? January, February, March, April, May, or June or type "all" to diplay data for all months?\n').lower()
    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month = input('Enter valid month\n').lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('\nWhich day wold you like to filter by? monday, tuesday, wednesday, thursday, friday, saturday , sunday or type "all" to display data of all days?\n').lower()
    while(True):
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday'         or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Enter Correct day: ').lower()


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

    # to_datetime is used to convert date into date format
    df['End Time'] = pd.to_datetime(df['End Time'])

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month]

    #filter data by day.
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    # display the most common day of week
    if(day == 'all'):
        most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(most_common_day))

    # display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    time_1 = total_travel
    day = time_1 // (24 * 3600)
    time_1 = time_1 % (24 * 3600)
    hour = time_1 // 3600
    time_1 %= 3600
    minutes = time_1 // 60
    time_1 %= 60
    seconds = time_1
    print("\nTotal travel time is {} days {} hours {} minutes {} seconds".format(day, hour, minutes, seconds))


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    time_2 = mean_travel
    day_2 = time_2 // (24 * 3600)
    time_2 = time_2 % (24 * 3600)
    hour_2 = time_2 // 3600
    time_2 %= 3600
    minutes_2 = time_2 // 60
    time_2 %= 60
    seconds_2 = time_2
    print("\nMean travel time is {} hours {} minutes {} seconds".format(hour_2, minutes_2, seconds_2))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")


    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #display the 5 lines of raw data if the user want 
    for start in range (0, 10000, 5):
        end = 5
        show_data = input('\nWould you like to view data? Enter yes or no\n').lower()
        if show_data == 'yes':
               end+=start
               print(df.iloc[start:end])
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
