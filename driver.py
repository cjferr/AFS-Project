# this is where the workout movements get read in and computed

# ideas: keep a dict with all of the attributes we have in the workout currently, and ensure that limits
# are in place so the value corresponding with the key does not go over the value we want
# (ie we don't end up with more than 3 ab exercises)

# is there a way to read in rows randomly?  Or how could we ensure things are not picked in the same order each time?
# Random variable with a probability of skipping rows?

# reading in will come from the data_out.csv file, use the csv reader module to do this (look up functions to shuffle the list once its read in)
import csv
from datetime import date
import random

# Function to check that the row is completely filled out


def print_list(list):
    for elt in list:
        print(elt[0])


def check_valid(row):
    for i in range(2, 8):
        if row[i] == "":
            return False
    return True


def add_movement(picked, workout_attributes, movement):
    for i in range(2, 6):
        # print(movement[i])
        workout_attributes[movement[i]] += 1
    picked.append(movement)


def pick_first(options, picked, workout_attributes):
    for elt in options:
        if len(picked) > 0:
            break
        if elt[4] == 'high impact' and workout_attributes[elt[4]] > 3:
            break
        if workout_attributes[elt[2]] > 5:
            break
        if workout_attributes[elt[3]] > 9 and elt[3] == 'strength':
            break
        if workout_attributes[elt[5]] > 8 and elt[5] == 'anterior':
            break
        if "left" in elt and len(picked) > 0:
            break
        if "right" in elt and len(picked) > 0:
            break
        add_movement(picked, workout_attributes, elt)

        return elt


def pick_second(options, picked, workout_attributes, movement1):
    # bug here: picking the same movement twice if left or right is in the name, but not picking the opposite side for it.
    if "left" in movement1[0] or "right" in movement1[0]:
        string = ""
        if "left" in movement1[0]:
            string = "left"
        else:
            string = "right"

        text = movement1[0].replace(string, '')
        for e2 in options:
            if text in e2[0]:
                add_movement(picked, workout_attributes, e2)
                return

    for elt in options:
        if len(picked) > 1:
            return
        elif movement1[2] == elt[2]:
            pass
        elif movement1[3] == 'cardio' and elt[3] == 'cardio':
            pass
        elif movement1[4] == 'high impact' and elt[4] == 'high impact':
            pass
        else:
            if elt[4] == 'high impact' and workout_attributes[elt[4]] > 3:
                pass
            elif workout_attributes[elt[2]] > 5:
                pass
            elif workout_attributes[elt[3]] > 9 and elt[3] == 'strength':
                pass
            elif workout_attributes[elt[5]] > 8 and elt[5] == 'anterior':
                pass
            elif "left" in elt or "right" in elt:
                pass
            else:
                add_movement(picked, workout_attributes, elt)


def pick_station_B(options, picked, workout_attributes):
    movement1 = pick_first(options, picked, workout_attributes)
    pick_second(options, picked, workout_attributes, movement1)

    # print(picked)


def scale_A(options, movement):

    for elt in options:
        pick = True
        if elt[0] == movement[0]:
            pass
        elif "left" in elt[0] and "left" not in movement[0]:
            pass
        elif "right" in elt[0] and "right" not in movement[0]:
            pass
        elif "left" not in elt[0] and "left" in movement[0]:
            pass
        elif "right" not in elt[0] and "right" in movement[0]:
            pass
        else:
            if elt[2] != movement[2]:
                pick = False
            # this if statement is never becoming true
            if pick:
                # print('adding movement A')
                return elt


def scale_C(options, movement, scale_a_first):

    for elt in options:
        pick = True
        if elt == movement or elt == scale_a_first:
            pass
        elif "left" in elt[0] and "left" not in movement[0]:
            pass
        elif "right" in elt[0] and "right" not in movement[0]:
            pass
        elif "left" not in elt[0] and "left" in movement[0]:
            pass
        elif "right" not in elt[0] and "right" in movement[0]:
            pass
        else:
            if elt[2] != movement[2] or elt[4] == 'high impact':
                pick = False
            # this if statement is never becoming true
            if pick:
                # print('adding movement C')
                return elt


def scale(options, picked):
    new_list = []
    scale_a_first = scale_A(options, picked[0])
    scale_c_first = scale_C(options, picked[0], scale_a_first)
    scale_a_second = scale_A(options, picked[1])
    scale_c_second = scale_C(options, picked[1], scale_a_second)

    # options.remove(scale_a_first)
    # options.remove(scale_c_first)
    # options.remove(scale_a_second)
    # options.remove(scale_c_second)

    new_list.append(scale_a_first[0])
    new_list.append(picked[0][0])
    new_list.append(scale_c_first[0])
    new_list.append(scale_a_second[0])
    new_list.append(picked[1][0])
    new_list.append(scale_c_second[0])
    # append the options to the new list in the right order
    # new_list += scale_a_first[0] + picked[0][0] + scale_c_first[0] + \
    #     scale_a_second[0] + picked[1][0] + scale_c_second[0]
    picked = new_list
    return picked


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
        elif row[6] == '1':
            one_options.append(row)
        elif row[6] == '2':
            two_options.append(row)
        elif row[6] == '3':
            three_options.append(row)
        elif row[6] == '4':
            four_options.append(row)
        elif row[6] == '5':
            five_options.append(row)
        elif row[6] == 'abs':
            abs_options.append(row)

random.shuffle(one_options)
random.shuffle(two_options)
random.shuffle(three_options)
random.shuffle(four_options)
random.shuffle(five_options)
random.shuffle(abs_options)
# creating the data structures required
# order of the list will be 1A, 1B, 1C, 2A, 2B, 2C
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

pick_station_B(one_options, one, workout_attributes)
pick_station_B(two_options, two, workout_attributes)
pick_station_B(three_options, three, workout_attributes)
pick_station_B(four_options, four, workout_attributes)
pick_station_B(five_options, five, workout_attributes)

# picking abs exercises
for elt in abs_options:
    if len(abs) > 1:
        break
    if ("left" in elt[0] or "right" in elt[0]) and len(abs) < 1:
        string = ""
        if "left" in elt[0]:
            string = "left"
        else:
            string = "right"

        text = elt[0].replace(string, '')
        for e2 in abs_options:
            if text in e2[0]:
                add_movement(abs, workout_attributes, e2)
    else:
        add_movement(abs, workout_attributes, elt)

# SCALING
one = scale(one_options, one)
two = scale(two_options, two)
three = scale(three_options, three)
four = scale(four_options, four)
five = scale(five_options, five)
abs = scale(abs_options, abs)

workout = []
workout += one + two + three + four + five + abs

for elt in workout:
    print(elt)

# with open('data_out.csv', 'w') as out_data:
#     with open('data_out.csv') as in_data:
#         write = csv.writer(out_data, delimiter=',', quotechar='|')
#         read = csv.reader(in_data, delimiter=',', quotechar='|')
#         for elt in read:
#             if elt[0] in workout:
#                 elt[1] = date
#         write.writerow(elt)

# order of the workout is A/B/C for station 1 exercise 1, then exercise 2, then station 2, etc. all the way around the gym

# print('Here is your workout!\n\n')
# print(one)
# print('\n')
# print(two)
# print('\n')
# print(three)
# print('\n')
# print(four)
# print('\n')
# print(five)
# print('\n')
# print(abs)

# have to still pick scaling options

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
