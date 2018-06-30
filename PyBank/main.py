# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv

csvpath = os.path.join('..', '..', 'UCBEL201806DATA2-Class-Repository-DATA', '03-Python', 'Homework', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSVs
counter = 0
profits = 0
max = 0
min = 0
first_num = 1154293
last_num = 883934
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for x in csvreader:
        counter += 1 # Total number of minths in data
        profits += int(x[1]) # Total net Amount over entire period
        if max < int(x[1]):
            max = int(x[1])
        if min > int(x[1]):
            min = int(x[1])
        avg = (last_num - first_num) / 40

print("Total number of months " + str(counter))
print("Profits are " + str(profits))
print("The maximun number is " + str(max))
print("The minimun number is  " + str(min))
print(avg)
