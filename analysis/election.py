import os
import csv

candidates = []
votes = []

csvpath = os.path.join(r'D:\python-challenge\Resources\election_data.csv')
print("Election Results")
print("----------------------------")

with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #find the number of rows in the csv file
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            
        votes.append(row[2])
    
    print("Total Votes: " + str(len(votes)))
    print("----------------------------")
    for cadidate in candidates:
        print(cadidate + ": " + str(round((votes.count(cadidate)/len(votes))*100,3)) + "% (" + str(votes.count(cadidate)) + ")")
    print("----------------------------")
    print("Winner: " + str(max(set(votes), key=votes.count)))
    print("----------------------------")