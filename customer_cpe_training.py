import csv

# Author: Mitchell Gulledge
# This script looks for duplicate emails indicating a customer has signed up for multiple events

master_list_all_emails = []


with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]}')
            #print(f'\t{row[1]}')



            # conditional statement to only filter for attended employees
            if row[0] == 'Attended':

                # appending row 1 to master list of emails
                master_list_all_emails.append(row[1])

                if len(row[2]) != 0:

                    # appending row 2 email to master_list_all_emails
                    master_list_all_emails.append(row[2])


            #master_list_all_emails.append(row[0])
            #master_list_all_emails.append(row[1])


            line_count += 1
    print(f'Processed {line_count} lines.')

print(len(master_list_all_emails))
print(len(set(master_list_all_emails)))



def getDupes(inp):
    dct = dict()
    for elem in inp:
        if elem in dct:
            dct[elem] += 1
        else:
            dct[elem] = 1
    dct = {key: value for key, value in dct.items() if value > 1}
    return dct

print(len(getDupes(master_list_all_emails)))


