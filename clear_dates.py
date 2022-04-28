# Simple script to clear the date of access column in the data at the end of the week

import csv

with open('data_out.csv') as info:
    with open('data_out.csv', 'w') as out:
        in_data = csv.reader(info, delimiter=',', quotechar='|')
        out_data = csv.writer(out, delimiter=',', quotechar='|')
        for row in in_data:
            print(row)
            # row[1] = ""
            # out_data.writerow(row)
