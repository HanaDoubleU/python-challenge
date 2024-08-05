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

    # initializing variable
    # tuesday's lecture
    totalmonths = 0

    # looping through rows in budget_data.csv
    # source: loop_de_loop_solution.py
    for row in csvreader:

        # counting rows in budget_data.csv for total months
        # hint from agustín
        totalmonths = totalmonths + 1

    # printing results in terminal
    # source: variables_solution.py
    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(totalmonths))
    # print("Total: " + str(total))
    # print("Average Change: " + str(averagechange))
    # print("Greatest Increase in Profits: " + str(giip))
    # print("Greatest Decrease in Profits: " + str(gdip))