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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

marketers = []

for row in calls: #Start by Listing all unique numbers that send calls
    if row[0] not in marketers:
        marketers.append(row[0])

for row in calls: #Filter out numbers that receive calls
    if row[1] in marketers:
        marketers.remove(row[1])
        
for row in texts: #Filter out numbers that send/receive texts
    if row[0] in marketers:
        marketers.remove(row[0])
    if row[1] in marketers:
        marketers.remove(row[1])


print("These numbers could be telemarketers: ")
print(*marketers, sep='\n')





