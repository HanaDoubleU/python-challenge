# importing election_data.csv
# source: cereal.py
import os
import csv

# election_data.csv's relative location
# source: cereal.py
election_data_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# opening election_data.csv for reading -- not writing
# source: graduation_fuctions.py
with open(election_data_csv, 'r') as csvfile:

    # separating data in election_data.csv by comma
    # source: graduation_functions.py
    csvreader = csv.reader (csvfile, delimiter=",")
    
    # storing header
    # source: graduation_functions.py
    header = next(csvreader)

    # initializing variable
    # tuesday's lecture
    totalvotes = 0

    # looping through rows in election_data.csv
    # source: loop_de_loop_solution.py
    for row in csvreader:

        # counting rows in election_data.csv for total votes
        # source: hint from agustín
        totalvotes = totalvotes + 1

    # printing results
    # source: variables_solution.py
    print("Election Results")
    print("------------------------------")
    print("Total Votes: " + str(totalvotes))
    # print("------------------------------")
    # print(firstcandidate + ": " + str(firstpercentage) + "(" + str(firsttotal) + ")")
    # print(secondcandidate + ": " + str(secondpercentage) + "(" + str(secondtotal) + ")")
    # print(thirdcandidate + ": " + str(thirdpercentage) + "(" + str(thirdtotal) + ")")
    # print("------------------------------")
    # print("Winner: " + winner)