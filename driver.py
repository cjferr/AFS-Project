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

# reading in the data and randomizing it
data = []
with open('data_out.csv') as info:
    in_data = csv.reader(info, delimiter=',', quotechar='|')
    for row in in_data:
        data.append(row)

random.shuffle(data)
print(data)

# Data structures:
# 1. map to store overall workout attributes
# 2. list for each station for the 2 movements that will be there
# 3. list storing all the data in the csv file

# things that need to get done:
# 1. read in the CSV file data row by row
# 2. check the attributes against our current map with our current attributes; does it invalidate any conditions? 2 cases then;
# 2a. if it invalidates, break and move onto the next row
# 2b. if not, check the date it was last picked.  If it wasn't this week, then we can pick it
