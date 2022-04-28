# this is where the workout movements get read in and computed

# ideas: keep a dict with all of the attributes we have in the workout currently, and ensure that limits
# are in place so the value corresponding with the key does not go over the value we want
# (ie we don't end up with more than 3 ab exercises)

# is there a way to read in rows randomly?  Or how could we ensure things are not picked in the same order each time?
# Random variable with a probability of skipping rows?

# reading in will come from the data_out.csv file, use the csv reader module to do this (look up functions to shuffle the list once its read in)
import csv
import random
import math

# Function to check that the row is completely filled out


def check_valid(row):
    for i in range(8):
        if row[i] is "":
            return False
    return True


def fill_station(station, options, workout_attributes):
    pass


# reading in the data and randomizing it
data = []
with open('data_out.csv') as info:
    in_data = csv.reader(info, delimiter=',', quotechar='|')
    for row in in_data:
        data.append(row)
random.shuffle(data)
# print(data)

# creating the data structures required
workout_attributes = {}
one = []
two = []
three = []
four = []
five = []
abs = []

# going through each movement in the data list
# row 0 is the exercise name
# row 1 is date of access
# row 2 is modality (we want no more than 4 of any one modality, and at least 1 of each)
# row 3 is cardio/strength (we want at least 3 cardio movements)
# row 4 is impact (no more than 3 impact movements)
# row 5 is anterior/posterior (at least 4 posterior movements)
# row 6 is station number (2 per)
# row 7 is equipment (I want this to be a list of everything in the cell seperated by commas)
count = 0
for row in data:
    # if we get to here that means the movement must have all parameters filled in
    if not check_valid(row):
        pass
    name = row[0]
    date = row[1]
    modality = row[2]
    weight_or_cardio = row[3]
    impact = row[4]
    front_back = row[5]
    station = row[6]
    equipment = str(row[7])
    if row[8] is not "":
        equipment += "," + row[8]
        equipment = equipment.split(',')

    # things we want to choose by: modality, station number,

    select = False

    # implement deciding if we want to make select true here

    if select:
        pass
        # implement choosing the movement for the exercise here

print(count)
# Data structures:
# 1. map to store overall workout attributes
# 2. list for each station for the 2 movements that will be there
# 3. list storing all the data in the csv file

# things that need to get done:
# 1. read in the CSV file data row by row
# 2. check the attributes against our current map with our current attributes; does it invalidate any conditions? 2 cases then;
# 2a. if it invalidates, break and move onto the next row
# 2b. if not, check the date it was last picked.  If it wasn't this week, then we can pick it
