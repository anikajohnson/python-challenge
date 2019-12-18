#Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# Lists to store data
    months[]
    profit[]
    profit_change = []
    avg_prof_change = []
    max_prof_change = []
    min_prof_change = []
    max_prof_change_date = []
    min_prof_change_date = []
   

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
for row in budget_csv:

    #assign to rows
    months.append(row[0])
    profit.append(row[1])

#print output
print("Financial Analysis")
print("-----------------------------------")
print("Total Months:", len(months))
print("Total: $", sum(profit))


for i in range(1, len(profit)):
    #The average of the changes in "Profit/Losses" over the entire period
    profit_change.append(profit[i]-profit[i-1])
    avg_change = sum(profit_change)/len(profit_change)

    #The greatest increase in profits (date and amount) over the entire period
    max_prof_change = max(prof_change)
    max_prof_change_date = str(month[prof_change.index(max(prof_change))])

    #The greatest decrease in losses (date and amount) over the entire period
    min_prof_change = min(prof_change)
    min_prof_change_date = str(month[prof_change.index(min(prof_change))])

#print output
print("Avereage Change: $", round(avg_prof_change))
print("Greatest Increase in Profits:", max_prof_change_date,"($", max_prof_change,")")
print("Greatest Decrease in Profits:", min_prof_change_date,"($", min_prof_change,")")
