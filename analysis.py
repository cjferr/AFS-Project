import collections
import csv

data = []
with open('Data_in.csv') as in_csv:
    in_data = csv.reader(in_csv, delimiter=',', quotechar='|')
    # enumerate let's you grab the index of the item
    for i, row in enumerate(in_data):
        data.append(row)


# makes a list with each element being the first column of each row in data (list comprehension)
exercises = [row[0] for row in data]

# class that does operator overloading to function like a map to track counts (works like a map in C++ for word counts as an example)
counter = collections.Counter()

# initialize values in the counter
for exercise in exercises:
    unique_words = set(exercise.lower().split())
    for word in unique_words:
        counter[word] += 1

# put the counter into a list so we can put it into a file, sort it in order of frequency
common_words = []
for word, count in counter.items():
    common_words.append((word, count))
common_words.sort(key=lambda x: -x[1])

# write the list into a text file

with open("common-words.txt", "w") as f:
    for word, count in common_words:
        f.write(f'{word}: {count}\n')
