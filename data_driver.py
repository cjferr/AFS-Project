# This file is where the workouts will be selected and scaled

# reads in the data
import json
import csv
import random
# row 0 is the exercise name
# row 1 is date of access
# row 2 is modality
# row 3 is cardio/strength
# row 4 is impact
# row 5 is anterior/posterior
# row 6 is station number
# row 7 is equipment

# how do i not overwrite the info for the equipment?  Like if i want to modify a cell but not delete the info how do I do that
data = []
with open('Data_in.csv') as in_csv:
    with open('data_out.csv', 'w') as out_csv:
        writer = csv.writer(out_csv, delimiter=',', quotechar='|')
        in_data = csv.reader(in_csv, delimiter=',', quotechar='|')
        bw_stations = [1, 4, 5]
        abs_stations = [4, "abs"]

        for i, row in enumerate(in_data):
            obj = row[0].lower()
            if "step" in obj and "ing" not in obj:
                row[6] = 2
                row[7] = "steps"
            if "crunch" in obj:
                row[2] = "abs"
                row[3] = "strength"
                row[4] = 0
                row[5] = "anterior"
            if "row" in obj:
                row[2] = "upper pull"
                row[3] = "strength"
                row[4] = 0
                row[5] = "posterior"
            if "barbell" in obj or "wp" in obj:
                row[6] = 4
                row[7] = "barbell"
                row[3] = "strength"
                row[4] = 0
            if "squat" in obj:
                row[2] = "lower push"
                if "front" in obj:
                    row[5] = "anterior"
                else:
                    row[5] = "posterior"
                if "jump" in obj:
                    row[3] = "cardio"
                else:
                    row[3] = "strength"
            if "lunge" in obj or "stepping" in obj:
                row[2] = "lower push"
                if "jump" in obj:
                    row[3] = "cardio"
                else:
                    row[3] = "strength"
                row[5] = "posterior"
            if "oh" in obj:
                row[2] = "upper push"
                row[3] = "strength"
                row[5] = "anterior"
            if "press" in obj:
                row[2] = "upper push"
                row[3] = "strength"
                row[5] = "anterior"
            if "jump" in obj or "hop" in obj or "skip" in obj:
                row[4] = 1
                row[3] = "cardio"
                row[2] = "lower push"
            if "db" in obj:
                row[7] = "db"
                row[6] = 1
                row[3] = "strength"
            if "plank" in obj:
                row[2] = "abs"
                row[4] = 0
                row[5] = "anterior"
            if "boxing" in obj:
                row[6] = 5
                row[7] = "boxing gear"
                row[3] = "cardio"
            if "suspension" in obj:
                row[6] = 3
                row[7] = "suspension"
                row[4] = 0
            if "curl" in obj:
                row[2] = "upper pull"
                row[3] = "strength"
                row[4] = 0
                row[5] = "anterior"
            if "press" in obj or 'push' in obj:
                row[2] = "upper push"
                row[3] = "strength"
                row[5] = "anterior"
            if "up" and "down" in obj:
                row[2] = "cardio"
                row[3] = "cardio"
                row[4] = 1
                row[5] = "anterior"
            if "mb" in obj:
                row[7] = "med ball"
                row[6] = 2
            if "band" in obj:
                row[7] = "band"
                row[6] = 4
            if "stability ball" in obj:
                row[7] = "stability ball"
                row[6] = 1
            if "v " in obj:
                row[2] = "abs"
                row[3] = "strength"
                row[5] = "anterior"
            if "hurdle" in obj:
                row[7] = "hurdle"
                row[6] = 5
            if row[7] is "":  # need to find a way where I can make sure things that are L and R are grouped together; maybe delete the right options and if it picks left than just tell them to make it alternating?
                row[6] = random.choice(bw_stations)
            if row[2] is "abs":
                row[6] = random.choice(abs_stations)

            writer.writerow(row)
            data.append(row)

        # print(row)
        # check how many cells are empty: use sum(not not x for x in a)
