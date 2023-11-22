"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

timespent = {}
longest_time = 0
longest_num = 0

for row in calls: #Add in any new unique tel no.
    if row[0] not in timespent:
        timespent.update({row[0]: int(row[3])})
    if row[1] not in timespent:
        timespent.update({row[1]: int(row[3])})
        
        #Add time to existing tel no.
    if row[0] in timespent:
        timespent.update({row[0]: (timespent.get(row[0]) + int(row[3]))})
    if row[1] in timespent:
        timespent.update({row[1]: (timespent.get(row[1]) + int(row[3]))})


for num in timespent: #Determine highest time spent
    if timespent.get(num) > longest_time:
        longest_time = timespent.get(num)
        longest_num = num


print("{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016."
      .format(telephone_number = longest_num, total_time = longest_time))