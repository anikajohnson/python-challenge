#Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Lists to store data

months = []    
profit = []
profit_change = []
avg_prof_change = []
max_prof_change = []
min_prof_change = []
max_prof_change_date = []
min_prof_change_date = []

# Read in the CSV file
with open(budget_csv) as budget_file:

    # Split the data on commas
    budget_reader = csv.reader(budget_file, delimiter=',')

    header = next(budget_reader)




#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
    for row in budget_reader:

        #assign to rows
        months.append(row[0])
        profit.append(float(row[1]))

#print output
print("Financial Analysis")
print("-----------------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: $ {round(sum(profit))}')


for i in range(1, len(profit)):
    #The average of the changes in "Profit/Losses" over the entire period
    profit_change.append(profit[i]-profit[i-1])
    avg_prof_change = sum(profit_change)/len(profit_change)

    #The greatest increase in profits (date and amount) over the entire period
    max_prof_change = max(profit_change)
    max_prof_change_date = str(months[profit_change.index(max(profit_change))])

    #The greatest decrease in losses (date and amount) over the entire period
    min_prof_change = min(profit_change)
    min_prof_change_date = str(months[profit_change.index(min(profit_change))])

#print to terminal 
print(f'Average Change: $ {round(avg_prof_change, 2)}')
print(f'Greatest Increase in Profits: {max_prof_change_date}($ {round(max_prof_change)})')
print(f'Greatest Decrease in Profits: {min_prof_change_date} ($ {round(min_prof_change)})')

#print to file
output_file = os.path.join("financial_analysis.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("-----------------------------------\n")
    datafile.write(f'Total Months: {len(months)}\n')
    datafile.write(f'Total: $ {round(sum(profit))}\n')
    datafile.write(f'Average Change: $ {round(avg_prof_change, 2)}\n')
    datafile.write(f'Greatest Increase in Profits: {max_prof_change_date} ($ {round(max_prof_change)})\n')
    datafile.write(f'Greatest Decrease in Profits: {min_prof_change_date} ($ {round(min_prof_change)})\n')
