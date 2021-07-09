import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    c
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    global month, day, city
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('what is the city you want to filter?'))
    while city not in CITY_DATA:
        print('Restart the program again with a valid city, chicago, new york city, washington')
        break
    else:
        # TO DO: get user input for month (all, january, february, ... , june)
        month = str(input('what is the month you want to filter?'))

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = str(input('what is the day you want to filter?'))
        print('-' * 40)
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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print("the most common month", df['month'].mode())

    # TO DO: display the most common day of week

    print('the most common day', df['day'].mode())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(df['hour'].mode())
    df['mintue_start'] = df['Start Time'].dt.minute

    df['hour_end'] = df['End Time'].dt.hour
    df['mintue_end'] = df['End Time'].dt.minute
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most commonly used start station', df['Start Station'].mode())

    # TO DO: display most commonly used end station
    print('the most commonly used end station', df['End Station'].mode())

    # TO DO: display most frequent combination of start station and end station trip
    print((df['Start Station'] + df['End Station']).mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['total travel time'] = (df['hour_end'] - df['hour']) * 60 + df['mintue_end'] - df['mintue_start']
    print('the total traveled time', df['total travel time'].sum())
    # TO DO: display mean travel time
    print('the mean travel time', df['total travel time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type)
    # TO DO: Display counts of gender
    if city == 'new york city':
        user_gender = df['Gender'].value_counts()
        print(user_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('the earliest', 'the recent', 'the most common', df['Birth Year'].min(), df['Birth Year'].max(),
              df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
