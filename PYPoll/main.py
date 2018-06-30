# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv

csvpath = os.path.join('..', '..', 'UCBEL201806DATA2-Class-Repository-DATA', '03-Python', 'Homework', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')

# # Method 1: Plain Reading of CSVs
cand_votes = {} 
counter = 0
percent_each = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for vote in csvreader:
        counter += 1
        if (vote[2]) in cand_votes.keys():
            cand_votes[vote[2]] += 1
        else: 
            cand_votes[vote[2]] = 1

percent = []
for key in cand_votes:
    percent_each = cand_votes[key]/counter *100
    percent.append(f"{key}:{percent_each}%")
winner = max(cand_votes, key=cand_votes.get)
print(cand_votes)
print(counter)
print(percent)
print(winner)