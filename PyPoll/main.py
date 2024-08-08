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

    # initializing variables
    # variables_solution.py
    firstcandidate = "random string"
    secondcandidate = "random string"
    thirdcandidate = "random string"
    firsttotal = 0
    secondtotal = 0
    thirdtotal = 0
    firstpercentage = 0
    secondpercentage = 0
    thirdpercentage = 0
    winner = "random string"

    # list
    # source: monday's slides
    candidates = []

    # looping through rows in election_data.csv
    # source: loop_de_loop_solution.py
    for row in csvreader:

        # counting rows in election_data.csv for total votes
        # source: hint from agustín
        totalvotes = totalvotes + 1

        # excluding header from conditional
        # conditionals_solution.py
        if totalvotes > 1:

            # conditional
            # source: conditionals_solution.py and xpert
            if row[2] not in candidates:
                
                # adding candidate to list
                # monday's list
                candidates.append(row[2])
            
    # re-initializing variables after adding candidate to list
    # variables_solution.py
    firstcandidate = candidates[0]
    secondcandidate = candidates[1]
    thirdcandidate = candidates[2]

    # re-set
    # source: xpert
    csvfile.seek(0)

    # storing header
    # graduation_fuctions.py and xpert
    header = next(csvreader)
    
    # looping through rows in election_data.csv
    # source: loop_de_loop_solution.py
    for row in csvreader:

        # conditional
        # source: conditionals_solution.py
        if row[2] == firstcandidate:
            firsttotal = firsttotal + 1
        elif row[2] == secondcandidate:
            secondtotal = secondtotal + 1
        else:
            thirdtotal = thirdtotal + 1
    
    # calculating percentages
    # source: basic skill from fifth grade
    firstpercentage = firsttotal / totalvotes * 100
    secondpercentage = secondtotal / totalvotes * 100
    thirdpercentage = thirdtotal / totalvotes * 100

    # winner
    # source: conditionals_solution.py and xpert
    if firstpercentage > secondpercentage and firstpercentage > thirdpercentage:
        winner = firstcandidate
    elif secondpercentage > firstpercentage and secondpercentage > thirdpercentage:
        winner = secondcandidate
    else:
        winner = thirdcandidate

    # printing results in terminal
    # source: variables_solution.py
    print("Election Results")
    print("------------------------------")
    print("Total Votes: " + str(totalvotes))

    # test, pt. 1: length of list
    # source: variables_solution.py and monday's slides
    # variables_solution.py and monday's slides
    # print(len(candidates))

    # test, pt. 2: according to terminal...
    # source: monday's slides
    # len(candidates) = 3

    # printing remaining results in terminal
    # source: variables_solution.py
    print("------------------------------")
    print(firstcandidate + ": " + str(round(firstpercentage, 3)) + "% " + "(" + str(firsttotal) + ")")
    print(secondcandidate + ": " + str(round(secondpercentage, 3)) + "% " + "(" + str(secondtotal) + ")")
    print(thirdcandidate + ": " + str(round(thirdpercentage, 3)) + "% " + "(" + str(thirdtotal) + ")")
    print("------------------------------")
    print("Winner: " + winner)
    print("------------------------------")

# results.txt's relative location
# source: cereal.py
results_txt = os.path.join("..", "PyPoll", "analysis", "results.txt")

# exporting results
# source: xpert
with open(results_txt, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------------------\n")
    txtfile.write("Total Votes: " + str(totalvotes) + "\n")
    txtfile.write("------------------------------\n")
    txtfile.write(firstcandidate + ": " + str(round(firstpercentage, 3)) + "% " + "(" + str(firsttotal) + ")\n")
    txtfile.write(secondcandidate + ": " + str(round(secondpercentage, 3)) + "% " + "(" + str(secondtotal) + ")\n")
    txtfile.write(thirdcandidate + ": " + str(round(thirdpercentage, 3)) + "% " + "(" + str(thirdtotal) + ")\n")
    txtfile.write("------------------------------\n")
    txtfile.write("Winner: " + winner + "\n")
    txtfile.write("------------------------------\n")
