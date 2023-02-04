This project explores data related to bike share systems for three major cities in the US (Chicago, New-York and Washington). The data is provided by 'Motivate', a bike share service provider in major cities
in the US. 

The data contains:

    -Start Time (e.g., 2017-01-01 00:07:57)
    -End Time (e.g., 2017-01-01 00:20:53)
    -Trip Duration (in seconds - e.g., 776)
    -Start Station (e.g., Broadway & Barry Ave)
    -End Station (e.g., Sedgwick St & North Ave)
    -User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

    -Gender
    -Birth Year
    
Statistics Computed



# 1 Popular times of travel (i.e., occurs most often in the start time)

    -most common month
    -most common day of week
    -most common hour of day

# 2 Popular stations and trip

    -most common start station
    -most common end station
    -most common trip from start to end (i.e., most frequent combination of start station and end station)

# 3 Trip duration

    -total travel time
    -average travel time

# 4 User info

    -counts of each user type
    -counts of each gender (only available for NYC and Chicago)
    -earliest, most recent, most common year of birth (only available for NYC and Chicago)

The project takes input from the user about the city, month, day of week and computes the statistics for it.
