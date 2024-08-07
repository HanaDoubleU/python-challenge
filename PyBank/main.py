# importing budget_data.csv
# source: cereal.py
import os
import csv

# budget_data.csv's relative location
# source: cereal.py
budget_data_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# opening budge_data.csv for reading -- not writing
# source: graduation_fuctions.py
with open(budget_data_csv, 'r') as csvfile:

    # separating data in budget_data.csv by comma
    # source: graduation_functions.py
    csvreader = csv.reader (csvfile, delimiter=",")
    
    # storing header
    # source: graduation_functions.py
    header = next(csvreader)

    # initializing variables
    # tuesday's lecture
    totalmonths = 0
    total = 0

    # initializing variable
    # tuesday's lecture and xpert
    previousvalue = 0

    # list
    # monday's slides and xpert
    changes = []

    # looping through rows in budget_data.csv
    # source: loop_de_loop_solution.py
    for row in csvreader:

        # counting lines except header in budget_data.csv for total months
        # hint from agustín
        totalmonths = totalmonths + 1

        # sum of second row's lines except header in budget_data.csv for total
        # xpert
        total = total + int(row[1])

        # excluding first row from conditional
        # xpert
        if totalmonths > 1:

            # remaining conditional
            # conditionals_solution.py and teaching assistant's solution
            change = int(row[1]) - previousvalue
            
            # adding change from one line and another to list
            # monday's slides
            changes.append(change)

        # re-initializing variable after conditional
        # xpert
        previousvalue = int(row[1])
        
    # calculating average change after loop
    # source: https://docs.python.org/3/library/functions.html#sum and xpert
    averagechange = sum(changes) / len(changes)


    # printing results in terminal
    # source: variables_solution.py
    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(totalmonths))
    print("Total: $" + str(total))
    
    # printing averagechange in terminal after rounding decimal
    # source: variables solution.py and xpert
    print("Average Change: $" + str(round(averagechange, 2)))

    # printing results in terminal
    # print("Greatest Increase in Profits: " + str(giip))
    # print("Greatest Decrease in Profits: " + str(gdip))