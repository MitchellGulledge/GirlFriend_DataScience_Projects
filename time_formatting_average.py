import csv
import json
import pandas as pd
from pandas import Series, DataFrame
import re

# creating function to find average value of a list
def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = float(sum_num) + float(t)          

    avg = float(sum_num) / len(num)
    return avg


# creating master list to hold all data that we can later average
master_time_list = []

# opening first csv file containing all the time formatted as 1 hour 16 min
# need to convert this to 01:16 etc
with open('time_data.csv') as csv_file:
    # setting delimiter as comma since we are working with csv file
    csv_reader = csv.reader(csv_file, delimiter=',')

    # iterating through each line of CSV file to fetch data
    for row in csv_reader:

        '''
        Each of the rows will be inside a list with a big string we can see some sample output 
        below of the rows, we just care about the first tuple and converting that to right format
        ['(9 minutes)']
        ['(1 hour 25 minutes),10/']
        ['(4 minutes)']
        ['(1 hour 41 minutes)']
        ['(7 minutes),10/16/2020']
        '''

        # going to replace the ['data'] to [data]
        list_of_times = str(row[0]).replace("'", "")

        # going to get all data in the row going up to minutes)
        # this way it is easier to delieniate whether the customer
        # was on for more than 1 hour
        x = list_of_times.rpartition('minutes)')
        parsed_time_output = str(x[0])[1:]

        # filtering out attendance for those who joined for a minute or two
        if parsed_time_output == 1 or parsed_time_output == 2 or parsed_time_output == '' or \
            parsed_time_output == 3 or parsed_time_output == 4 or parsed_time_output == 5:
            continue

        # setting conditional statement to see if hour is in output
        elif 'hour' in parsed_time_output and len(parsed_time_output) > 1:

            # replacing the hour with :
            cleaned_up_time = parsed_time_output.replace(' hour ', ":")
            #print(cleaned_up_time)

            # the first indexed element will be the amount of hours someone attended event
            # we can always assume 0 since there will never be a 10 hr event
            # going to multiply the amount of hours by 60 so we can get minutes
            hours_to_minutes = int(parsed_time_output[0]) * 60

            split_time = cleaned_up_time.split(':')
            #print(int(split_time[1]) + int(hours_to_minutes))
            total_minutes = int(split_time[1]) + int(hours_to_minutes)

            # appending minutes value to master_time_list
            master_time_list.append(total_minutes)

        # for everything under an hour we will add 0: in front of output
        else:

            # appending parsed time output to master_time_list to later be averaged
            master_time_list.append(parsed_time_output)


# running function to find average number of minutes in list
print(cal_average(master_time_list))
