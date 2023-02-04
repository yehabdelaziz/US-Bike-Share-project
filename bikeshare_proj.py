import pandas as pd 
import time


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    
    # get user input for city (chicago, new york city, washington). 
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city=input('which city?\n').lower()
        if city not in CITY_DATA:
        	print('Sorry {} is not in our database'.format(city))
        	continue
        else:
        	break

    # get user input for month (all, january, february, ... , june)
    months = ['All','January', 'February', 'March', 'April', 'May', 'June']
    while True:
        month=input('Which month do you want to filter? if not type all\n').title()
        if month not in months:
            print('Please enter a valid month')
            continue
        else: 
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['All','Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday']
    while True:
        day=input('Which day do you want to filter? if not type all\n').title()
        if day not in days:
            print('Please enter a valid day')
            continue
        else: 
            break

    print('-'*40)
    return city, month, day





def load_data(city, month, day):

    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['hour']=df['Start Time'].dt.hour
    df['month']=df['Start Time'].dt.month_name()
    df['day of week']=df['Start Time'].dt.day_name()
    if month!='All':
    	df=df[df['month']==month]
    if day!='All':
    	df=df[df['day of week']==day]

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month, day of week and hour
    if month=='All':
        print('The most frequent month is {}\n'.format(df['month'].mode()[0]))    
    if day=='All':
        print('The most frequent day of week is {}\n'.format(df['day of week'].mode()[0]))
    
    print('The most frequent hour is {}\n'.format(df['hour'].mode()[0]))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)







def station_stats(df):
    
    #Display the most common start station, end station and the most common combinations of them
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('The most frequent start station is {}\n'.format(df['Start Station'].mode()[0]))    


    print('The most frequent end station is {}\n'.format(df['End Station'].mode()[0]))    

    
    df2=df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination is {} and {} \n'.format(df2[0],df2[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #Display the total trip duration
    print('Total time of travel is {} hours\n'.format(df['Trip Duration'].sum()/3600))
    


    #Display the mean trip duration
    print('Mean time of travel is {} hours\n'.format(df['Trip Duration'].mean()))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    df2=df['User Type'].value_counts()
    print('There are {} {} and {} {} '.format(df2[0],df2.index[0],df2[1],df2.index[1]))

    # Display counts of gender
    if city=='chicago' or city=='new york':
        print('The number of males is {} and the number of females is {}'.format(df['Gender'].value_counts()[0],df['Gender'].value_counts()[1]))

    # Display earliest, most recent, and most common year of birth
        print('The earliest, most recent and the most common years of birth are {}, {} and {} respectively '.format(df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw(df):
    start_loc=0
    while True:
        show_raw=input('Do you want to see 5 rows of data? enter yes or no.\n')
        if show_raw.lower()=='yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5
        elif show_raw.lower()=='no':
            break
        else:
            print('\nPlease enter a valid input.\n')





city, month, day = get_filters()
df = load_data(city, month, day)
time_stats(df)
station_stats(df)
trip_duration_stats(df)
user_stats(df)
display_raw(df)

