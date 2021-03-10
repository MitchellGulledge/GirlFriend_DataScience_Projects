import csv
import json
import pandas as pd
# import Numpy and matplotlib 
from matplotlib import pyplot as plt 
import numpy 
import matplotlib
from pandas import Series, DataFrame
import seaborn as sns 


# creating master test list to store all webinar event data
master_test_list = []

# opening first of 2 files containing webinar data
with open('Webinars.csv') as csv_file:
    # setting delimiter as comma since we are working with csv file
    csv_reader = csv.reader(csv_file, delimiter=',')
    # creating line count variables to we can indicate how many rows we iterated through
    line_count = 0
    # iterating through each line of CSV file to fetch data
    for row in csv_reader:
        # if the line count is 0 we are on the first line and want to skip it
        if line_count == 0:
            # incrementing line count variable
            line_count += 1
        else:
            # incrementing line count variable
            line_count += 1
            # filterin for webinars that were sub event type Always-on Webinar
            if 'Always-on Webinar' == row[4] and row[30] != '':

                # appending month and attendance value to master_test_list
                master_test_list.append([str(row[1]).lower(), row[30]])

# opening second of 2 files containing webinar data
with open('Webinars3.csv') as csv2_file:
    # setting delimiter as comma since we are working with csv file
    csv2_reader = csv.reader(csv2_file, delimiter=',')
    # creating line count variables to we can indicate how many rows we iterated through
    line_count2 = 0
    # iterating through each line of CSV file to fetch data
    for row2 in csv2_reader:
        # if the line count is 0 we are on the first line and want to skip it
        if line_count2 == 0:
            # incrementing line count variable
            line_count2 += 1
        else:
            # incrementing line count variable
            line_count2 += 1
            # filterin for webinars that were sub event type Always-on Webinar
            if 'Always-on Webinar' == row2[9] and row2[19] != '' and 'n/a' not in row2[19]:

                # appending month and attendance value to master_test_list
                master_test_list.append([str(row2[1])[0:3].lower(), row2[19]])




# using list comprehension to get list of attendees for each month
jan_list = [int(y) for x, y in master_test_list if x == 'jan']
feb_list = [int(y) for x, y in master_test_list if x == 'feb']
mar_list = [int(y) for x, y in master_test_list if x == 'mar']
apr_list = [int(y) for x, y in master_test_list if x == 'apr']
may_list = [int(y) for x, y in master_test_list if x == 'may']
jun_list = [int(y) for x, y in master_test_list if x == 'jun']
jul_list = [int(y) for x, y in master_test_list if x == 'jul']
aug_list = [int(y) for x, y in master_test_list if x == 'aug']
sep_list = [int(y) for x, y in master_test_list if x == 'sep']
oct_list = [int(y) for x, y in master_test_list if x == 'oct']
nov_list = [int(y) for x, y in master_test_list if x == 'nov']
dec_list = [int(y) for x, y in master_test_list if x == 'dec']

# organizing data set to begin with may 2020 to feb 2021 and calculating sum for each list in the month
data_set2 = [sum(may_list), sum(jun_list), sum(jul_list), sum(aug_list), sum(sep_list), \
    sum(oct_list), sum(nov_list), sum(dec_list), sum(jan_list), sum(feb_list)]    

print(f'Number of attendees for each month starting may 2020 and ending feb 2021: {data_set2}')
print('Total number of attendees since program started: '+ str(sum(data_set2)))

# creating x axis list for graph
months = ['may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'jan', 'feb']


# Creating our own dataframe 
data = {"Month": months, 
        "Attendance": data_set2} 
  
# Now convert this dictionary type data into a pandas dataframe 
# specifying what are the column names 
df = pd.DataFrame(data, columns=['Month', 'Attendance']) 
  
  
# Defining the plot size 
plt.figure(figsize=(10, 8)) 
  
# Defining the values for x-axis, y-axis 
# and from which datafarme the values are to be picked 
plots = sns.barplot(x="Month", y="Attendance", data=df, color='orange') 
  
# Iterrating over the bars one-by-one 
for bar in plots.patches: 
    
    # Using Matplotlib's annotate function and 
    # passing the coordinates where the annotation shall be done 
    plots.annotate(format(int(bar.get_height())),      
    #plots.annotate(format(bar.get_height(), '.2f'),  
                   (bar.get_x() + bar.get_width() / 2,  
                    bar.get_height()), ha='center', va='center', 
                   size=15, xytext=(0, 5), 
                   textcoords='offset points',
                   ) 
  
  
# Setting the title for the graph 
plt.title("Webinar Attendance Data") 
  
# Fianlly showing the plot 
plt.show() 
