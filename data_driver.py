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

# how do i not overwrite the info for the equipment?  Like if i want to modify a cell but not delete the
# info how do I do that (I want to seperate each equipment by comma to split it into a list later on in the driver)


def append_to_cell(row, index, text):
    if row[index] is "":
        row[index] = text
    elif text == row[index]:
        pass
    else:
        row[index + 1] = text
    return


data = []
with open('Data_in.csv') as in_csv:
    with open('data_out.csv', 'w') as out_csv:
        writer = csv.writer(out_csv, delimiter=',', quotechar='|')
        reader = csv.reader(in_csv, delimiter=',', quotechar='|')
        bw_stations = [1, 4, 5]
        abs_stations = [4, "abs"]

        for i, row in enumerate(reader):
            obj = row[0].lower()
            if "run" in obj:
                row[2] = "lower pull"
                row[3] = "cardio"
                row[4] = "high impact"
                row[5] = "posterior"
                if "step" in obj:
                    row[6] = 2
                    append_to_cell(row, 7, "steps")
            if "step" in obj and "stepping" not in obj:
                row[6] = 2
                append_to_cell(row, 7, "steps")
                if "up" in obj:
                    row[2] = "lower push"
                    row[3] = "strength"
                    row[4] = "low impact"
                    row[5] = "posterior"
            if "press" in obj:
                row[2] = "upper push"
                row[3] = "strength"
                row[5] = "anterior"
            if "oh" in obj:
                row[2] = "upper push"
                row[3] = "strength"
                row[5] = "anterior"
            if "crunch" in obj:
                row[2] = "abs"
                row[3] = "strength"
                row[4] = "low impact"
                row[5] = "anterior"
            if "row" in obj:
                row[2] = "upper pull"
                row[3] = "strength"
                row[4] = "low impact"
                row[5] = "posterior"
            if "curl" in obj:
                row[2] = "upper pull"
                row[3] = "strength"
                row[4] = "low impact"
                row[5] = "anterior"
            if "barbell" in obj or "bb" in obj:
                row[6] = 4
                append_to_cell(row, 7, "barbell")
                row[3] = "strength"
                row[4] = "low impact"
            if "wp" in obj:
                append_to_cell(row, 7, "plate")
                row[3] = "strength"
                row[4] = "low impact"
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
            if "jump" in obj or "hop" in obj or "skip" in obj:
                row[4] = "high impact"
                row[3] = "cardio"
                row[2] = "lower push"
            elif i == 0:
                pass
            else:
                row[4] = "low impact"
            if "db" in obj:
                append_to_cell(row, 7, "db")
                row[6] = 1
                row[3] = "strength"
            if "plank" in obj:
                row[2] = "abs"
                row[4] = "low impact"
                row[5] = "anterior"
            if "boxing" in obj:
                row[6] = 5
                append_to_cell(row, 7, "boxing gear")
                row[3] = "cardio"
                row[2] = "upper push"
                row[5] = "anterior"
            if "suspension" in obj or "strap" in obj:
                row[6] = 3
                append_to_cell(row, 7, "suspension")
                row[4] = "low impact"
            if "press" in obj or 'push' in obj:
                row[2] = "upper push"
                row[3] = "strength"
                row[5] = "anterior"
            if "up" in obj and "down" in obj:
                row[2] = "upper push"
                row[3] = "cardio"
                row[4] = "high impact"
                row[5] = "anterior"
            if "mb" in obj:
                append_to_cell(row, 7, "med ball")
                row[6] = 2
            if "band" in obj:
                row[7] = "band"
                row[6] = 4
            if "stability ball" in obj:
                append_to_cell(row, 7, "stability ball")
                row[6] = 1
            if "bridge" in obj:
                row[2] = "lower push"
                row[3] = "strength"
                row[4] = "low impact"
                row[5] = "posterior"
            if "v " in obj:
                row[2] = "abs"
                row[3] = "strength"
                row[5] = "anterior"
            if "hurdle" in obj:
                append_to_cell(row, 7, "hurdle")
                row[6] = 5
            if "extension" in obj:
                if "tricep" in obj or "oh" in obj:
                    row[2] = "upper push"
                else:
                    row[2] = "lower push"
                row[3] = "strength"
                row[4] = "low impact"
                row[5] = "posterior"
            if "versa" in obj:
                append_to_cell(row, 7, "versabag")
                row[6] = 4
            if "ladder" in obj:
                row[6] = 4
                append_to_cell(row, 7, "ladder")
                row[2] = "lower push"
                row[3] = "cardio"
                row[4] = "low impact"
                row[5] = "posterior"
            if "wall sit" in obj:
                row[2] = "lower push"
                row[3] = "strength"
                row[4] = "low impact"
                row[5] = "anterior"
            if "chop" in obj:
                row[5] = "anterior"
            if "step" in obj and "stepping" not in obj:
                row[6] = 2
                append_to_cell(row, 7, "steps")
                if "up" in obj:
                    row[2] = "lower push"
                    row[3] = "strength"
                    row[4] = "low impact"
                    row[5] = "posterior"
            if "sandbell" in obj:
                row[7] = "sandbell"
                row[6] = 4
            if row[7] is "":  # need to find a way where I can make sure things that are L and R are grouped together; maybe delete the right options and if it picks left than just tell them to make it alternating?
                row[6] = random.choice(bw_stations)
                row[7] = "BW"
            if row[2] is "abs":
                row[6] = random.choice(abs_stations)

            writer.writerow(row)
            data.append(row)

        # print(sum(not not x for x in data))

        # print(row)
        # check how many cells are empty: use sum(not not x for x in a)
