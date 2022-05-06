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
    if row[index] == "":
        row[index] = text
    elif text == row[index]:
        pass
    else:
        row[index + 1] = text
    return


data = []


def fill_cell(row, col_idx, content):
    if not row[col_idx]:
        row[col_idx] = content


with open('Data_in.csv') as in_csv:
    with open('data_out.csv', 'w') as out_csv:
        writer = csv.writer(out_csv, delimiter=',', quotechar='|')
        reader = csv.reader(in_csv, delimiter=',', quotechar='|')
        bw_stations = [1, 4, 5]
        abs_stations = [4, "abs"]

        for i, row in enumerate(reader):
            obj = row[0].lower()
            if "run" in obj:
                fill_cell(row, 2, "lower pull")

                fill_cell(row, 3, "cardio")
                fill_cell(row, 4, "high impact")
                fill_cell(row, 5, "posterior")
                if "step" in obj:
                    fill_cell(row, 6, 2)
                    append_to_cell(row, 7, "steps")
            if "step" in obj and "stepping" not in obj:
                fill_cell(row, 6, 2)
                append_to_cell(row, 7, "steps")
                if "up" in obj:
                    fill_cell(row, 2, "lower push")
                    fill_cell(row, 3, "strength")
                    fill_cell(row, 4, "low impact")
                    fill_cell(row, 5, "posterior")
            if "press" in obj:
                fill_cell(row, 2, "upper push")
                fill_cell(row, 3, "strength")
                fill_cell(row, 5, "anterior")
            if "oh" in obj:
                fill_cell(row, 2, "upper push")
                fill_cell(row, 3, "strength")
                fill_cell(row, 5, "anterior")
            if "crunch" in obj:
                fill_cell(row, 2, "abs")
                fill_cell(row, 3, "strength")
                fill_cell(row, 4, "low impact")
                fill_cell(row, 5, "anterior")
            if "row" in obj:
                fill_cell(row, 2, "upper pull")
                fill_cell(row, 3, "strength")
                fill_cell(row, 4, "low impact")
                fill_cell(row, 5, "posterior")
            if "curl" in obj:
                fill_cell(row, 2, "upper pull")
                fill_cell(row, 3, "strength")
                fill_cell(row, 4, "low impact")
                fill_cell(row, 5, "anterior")
            if "barbell" in obj or "bb" in obj:
                fill_cell(row, 6, 4)
                append_to_cell(row, 7, "barbell")
                fill_cell(row, 3, "strength")
                fill_cell(row, 4, "low impact")
            if "wp" in obj:
                append_to_cell(row, 7, "plate")
                fill_cell(row, 3, "strength")
                fill_cell(row, 4, "low impact")
            if "squat" in obj:
                fill_cell(row, 2, "lower push")
                if "front" in obj:
                    fill_cell(row, 5, "anterior")
                else:
                    fill_cell(row, 5, "posterior")
                if "jump" in obj:
                    fill_cell(row, 3, "cardio")
                else:
                    fill_cell(row, 3, "strength")
            if "lunge" in obj or "stepping" in obj:
                fill_cell(row, 2, "lower push")
                if "jump" in obj:
                    fill_cell(row, 3, "cardio")
                else:
                    fill_cell(row, 3, "strength")
                fill_cell(row, 5, "posterior")
            if "jump" in obj or "hop" in obj or "skip" in obj:
                fill_cell(row, 4, "high impact")
                fill_cell(row, 3, "cardio")
                fill_cell(row, 2, "lower push")
            elif i == 0:
                pass
            else:
                fill_cell(row, 4, "low impact")
            if "db" in obj:
                append_to_cell(row, 7, "db")
                fill_cell(row, 6, 1)
                fill_cell(row, 3, "strength")
            if "plank" in obj:
                fill_cell(row, 2, "abs")
                fill_cell(row, 4, "low impact")
                fill_cell(row, 5, "anterior")
            if "boxing" in obj:
                fill_cell(row, 6, 5)
                append_to_cell(row, 7, "boxing gear")
                fill_cell(row, 3, "cardio")
                fill_cell(row, 2, "upper push")
                fill_cell(row, 5, "anterior")
            if "suspension" in obj or "strap" in obj:
                fill_cell(row, 6, 3)
                append_to_cell(row, 7, "suspension")
                fill_cell(row, 4, "low impact")
            if "press" in obj or 'push' in obj:
                fill_cell(row, 2, "upper push")
                fill_cell(row, 3, "strength")
                fill_cell(row, 5, "anterior")
            if "up" in obj and "down" in obj:
                fill_cell(row, 2, "upper push")
                fill_cell(row, 3, "cardio")
                fill_cell(row, 4, "high impact")
                fill_cell(row, 5, "anterior")
            if "mb" in obj:
                append_to_cell(row, 7, "med ball")
                fill_cell(row, 6, 2)
            if "band" in obj:
                fill_cell(row, 7, "band")
                fill_cell(row, 6, 4)
            if "stability ball" in obj:
                append_to_cell(row, 7, "stability ball")
                fill_cell(row, 6, 1)
            if "bridge" in obj:
                fill_cell(row, 2, "lower push")
                fill_cell(row, 3, "strength")
                fill_cell(row, 4, "low impact")
                fill_cell(row, 5, "posterior")
            if "v " in obj:
                fill_cell(row, 2, "abs")
                fill_cell(row, 3, "strength")
                fill_cell(row, 5, "anterior")
            if "hurdle" in obj:
                append_to_cell(row, 7, "hurdle")
                fill_cell(row, 6, 5)
            if "extension" in obj:
                if "tricep" in obj or "oh" in obj:
                    fill_cell(row, 2, "upper push")
                else:
                    fill_cell(row, 2, "lower push")
                fill_cell(row, 3, "strength")
                fill_cell(row, 4, "low impact")
                fill_cell(row, 5, "posterior")
            if "versa" in obj:
                append_to_cell(row, 7, "versabag")
                fill_cell(row, 6, 4)
            if "ladder" in obj:
                fill_cell(row, 6, 4)
                append_to_cell(row, 7, "ladder")
                fill_cell(row, 2, "lower push")
                fill_cell(row, 3, "cardio")
                fill_cell(row, 4, "low impact")
                fill_cell(row, 5, "posterior")
            if "wall sit" in obj:
                fill_cell(row, 2, "lower push")
                fill_cell(row, 3, "strength")
                fill_cell(row, 4, "low impact")
                fill_cell(row, 5, "anterior")
            if "chop" in obj:
                fill_cell(row, 5, "anterior")
            if "step" in obj and "stepping" not in obj:
                fill_cell(row, 6, 2)
                append_to_cell(row, 7, "steps")
                if "up" in obj:
                    fill_cell(row, 2, "lower push")
                    fill_cell(row, 3, "strength")
                    fill_cell(row, 4, "low impact")
                    fill_cell(row, 5, "posterior")
            if "sandbell" in obj:
                fill_cell(row, 7, "sandbell")
                fill_cell(row, 6, 4)
            if row[7] == "":  # need to find a way where I can make sure things that are L and R are grouped together; maybe delete the right options and if it picks left than just tell them to make it alternating?
                fill_cell(row, 6, random.choice(bw_stations))
                fill_cell(row, 7, "BW")
            if row[2] == "abs":
                fill_cell(row, 6, random.choice(abs_stations))

            writer.writerow(row)
            data.append(row)

        # print(sum(not not x for x in data))

        # print(row)
        # check how many cells are empty: use sum(not not x for x in a)
