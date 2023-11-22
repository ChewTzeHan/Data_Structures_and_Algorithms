"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

textunique, callunique = [], []

for row in texts: #All unique numbers in texts
    if row[0] not in textunique:
        textunique.append(row[0])
    if row[1] not in textunique:
        textunique.append(row[1])

for row in calls: #All unique numbers in calls
    if row[0] not in textunique:
        callunique.append(row[0])
    if row[1] not in textunique:
        callunique.append(row[1])


print("There are {count} different telephone numbers in the records."
      .format(count = (len(textunique) + len(callunique))))