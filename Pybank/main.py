import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_data.csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# "Date" and "Profit/Losses".

# Determine the total number of months in the data set
Total_Months = 

Print("Total Months")

# Calculate the net total amount of "Profit/Losses" over the entire period
Total_Profit_Losses = 

Print("Total")


# Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
Profit_Loss_Changes = 
Average_Change = 
    
Print("Average Change")

# Determine the greatest increase in profits (date and amount) over the entire period
Greatest_Profit_Increase = dict()

Print("Greatest Increase in Profits")

# Determine the greatest decrease in profits (date and amount) over the entire period
Greatest_Profit_decrease = dict()

Print("Greatest Decrease in Profits")


