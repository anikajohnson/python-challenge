#Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Define the function and have it accept the 'budget_data' as its sole parameter
def print_totals (budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    months = str(budget_data[0])
    profit = int(budget_data[1])


# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if name_to_check == row[0]:
            print_percentages(row)

#The total number of months included in the dataset
total_months =

#The net total amount of "Profit/Losses" over the entire period


#The average of the changes in "Profit/Losses" over the entire period


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period