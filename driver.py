# This file is where the workouts will be selected and scaled

# reads in the data
import csv
with open('Data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        print((row))
