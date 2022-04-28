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
    for i in range(2, 8):
        if row[i] is "":
            return False
    return True


def add_movement(one, workout_attributes, movement):
    for i in range(2, 5):
        # print(movement[i])
        workout_attributes[movement[i]] += 1
    one.append(movement[0])


def pick_station_one(options, one, workout_attributes):
    while len(one) < 3:
        for elt in options:
            if elt[4] == 'high impact' and workout_attributes[elt[4]] > 3:
                break
            if workout_attributes[elt[2]] > 5:
                break
            if workout_attributes[elt[3]] > 9 and elt[3] == 'strength':
                break
            if workout_attributes[elt[5]] > 8 and elt[5] == 'anterior':
                break
            if "left" in elt and len(one) > 0:
                break
            add_movement(one, workout_attributes, elt)

            if "left" in elt:
                text = elt.replace('left', '')
                for e2 in options:
                    if text in e2[0]:
                        add_movement(one, workout_attributes, elt)
    print(one)


# row 0 is the exercise name
# row 1 is date of access
# row 2 is modality (we want no more than 4 of any one modality, and at least 1 of each)
# row 3 is cardio/strength (we want at least 3 cardio movements)
# row 4 is impact (no more than 3 impact movements)
# row 5 is anterior/posterior (at least 4 posterior movements)
# row 6 is station number (2 per)
# row 7 is equipment (I want this to be a list of everything in the cell seperated by commas)

# reading in the data and randomizing it
one_options = []
two_options = []
three_options = []
four_options = []
five_options = []
abs_options = []

with open('data_out.csv') as info:
    in_data = csv.reader(info, delimiter=',', quotechar='|')
    for row in in_data:
        if not check_valid(row):
            pass
        elif row[6] is '1':
            one_options.append(row)
        elif row[6] is '2':
            two_options.append(row)
        elif row[6] is '3':
            three_options.append(row)
        elif row[6] is '4':
            four_options.append(row)
        elif row[6] is '5':
            five_options.append(row)
        elif row[6] is 'abs':
            abs_options.append(row)

random.shuffle(one_options)
random.shuffle(two_options)
random.shuffle(three_options)
random.shuffle(four_options)
random.shuffle(five_options)
random.shuffle(abs_options)
# creating the data structures required
workout_attributes = {}
one = []
two = []
three = []
four = []
five = []
abs = []

# init map with the key words from the dataset
with open('keywords.txt') as keywords:
    for word in keywords:
        word = word.replace('\n', '')
        workout_attributes[word] = 0

print(workout_attributes)

print("\n\n testing function pick_station_one\n")
pick_station_one(one_options, one, workout_attributes)
# going through each movement in the data list
# row 0 is the exercise name
# row 1 is date of access
# row 2 is modality (we want no more than 4 of any one modality, and at least 1 of each)
# row 3 is cardio/strength (we want at least 3 cardio movements)
# row 4 is impact (no more than 3 impact movements)
# row 5 is anterior/posterior (at least 4 posterior movements)
# row 6 is station number (2 per)
# row 7 is equipment (I want this to be a list of everything in the cell seperated by commas)

# things we want to choose by: modality, station number,

# implement deciding if we want to make select true here

# implement choosing the movement for the exercise here
# Data structures:
# 1. map to store overall workout attributes
# 2. list for each station for the 2 movements that will be there
# 3. list storing all the data in the csv file

# things that need to get done:
# 1. read in the CSV file data row by row
# 2. check the attributes against our current map with our current attributes; does it invalidate any conditions? 2 cases then;
# 2a. if it invalidates, break and move onto the next row
# 2b. if not, check the date it was last picked.  If it wasn't this week, then we can pick it
