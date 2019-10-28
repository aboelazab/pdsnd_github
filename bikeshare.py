import time
import pandas as pd

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ('chicago', 'new york city', 'washington')
        city = input("Which City would you like to explore its data? (Chicago, New York City, Washington) ").lower()
        if city in cities:
            print(city.title())
            break 
        else:
            print("{} is not a valid input!".format(city.title()))
            

    # get user input for month (all, january, february, ... , june)
    while True:
        mon = ('january', 'february', 'march', 'april', 'may', 'june')
        month = input("Which month would you like to explore? all, January, February, ... , June ").lower()
        if month == "all":
            break
        elif month in mon:
            print(month.title())
            break    
        else:
            print("{} is not a valid input!".format(month.title()))                 

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        day = input("Which day? (all, Monday, Tuesday, ... Sunday) ").lower()
        if day == "all":
            break
        elif day in days:
            print(day.title())
            break
        else:
            print("That's not a valid input!")
       

    print('-'*100)
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
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Combined stations'] = df['Start Station'] + ' to ' + df['End Station']
    

    if month != 'all':
        months = ['january', 'february', 'march','april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != "all":
        df = df[df['day_of_week'] == day.title()]    


    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]


    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    
    print("\nThe most common month: {}".format(common_month))
    print("\nThe most common day of week: ",common_day)
    print("\nThe most common start hour: ",common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]


    # display most frequent combination of start station and end station trip
    most_combined_stations = df['Combined stations'].mode()[0]
    


    print("\nThe most commonly used start station: ",common_start_station)
    print("\nThe most commonly used end station: ",common_end_station)
    print("\nThe most common trip: ",most_combined_stations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = np.sum(df['Trip Duration'])


    # display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])

    print("\nTotal travel time: ",(total_travel_time/60)," mins")
    print("\nAvg travel time: ", (mean_travel_time/60), " mins")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def user_stats(df):
    """
    Displays statistics on bikeshare users.
    HINT:
         user stats are not applicable in Washington City data
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()

    # Display counts of gender
    gender_count = df['Gender'].value_counts()
    

    # Display earliest, most recent, and most common year of birth
    earlies_year_of_birth = int(df['Birth Year'].min())
    most_recent_year_of_birth = int(df['Birth Year'].max())
    most_common_year_of_birth =  int(df['Birth Year'].mode()[0])

    print(user_types_count,"\n")
    
    print(gender_count)
    print("\nThe earliest year of birth: ",earlies_year_of_birth)
    print("\nThe most recent year of birth: ",most_recent_year_of_birth)
    print("\nThe most common year of birth: ",most_common_year_of_birth)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if city == "washington":
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)    
        

        raw = input("\nWould you like to see individual trip data? Type 'Yes' or 'No'. ")
        if raw.lower() == "yes":
            print(df.head())
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



    


if __name__ == "__main__":
	main()


    

 
