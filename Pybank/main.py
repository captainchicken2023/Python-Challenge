import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_data.csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(f"CSV Header: {csvheader}")
    
    # Create dictionary using CSV values
    csvreader = csv.Dict(budget_data)

# Define variables

Total_Months = 0 
Month_Changed = []
Previous_Change = 0
Profit_Loss_Changes = 0
Profit_Loss_Changes_list = []
Greatest_Profit_Increase = ["", 0]
Greatest_Profit_Decrease = ["", 999999999999999999999999999999]


# Determine the total number of months in the data set
Total_Months = Total_Months + 1

Print("Total_Months")

# Calculate the net total amount of "Profit/Losses" over the entire period
Total_Profit_Losses = Total_Profit_Losses +int(row["Revenue"])

Print("Total_Profit_Losses")


# Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes

Profit_Loss_Changes = int(row["Profit/Losses"]) - Previous_Change
Previous_Change = int(row["Profit/Losses"])
Profit_Loss_Changes_list = Profit_Loss_Changes_list +[Previous_Change]
Month_Changed = Month_Changed + [row["Date"]]
    
Average_Change = sum(Profit_Loss_Changes_list) / len(Profit_Loss_Changes_list)

Print("Average_Change")

# Determine the greatest increase in profits (date and amount) over the entire period

if (Profit_Loss_Changes > greatest increase[1]):
    greatest increase[0] = row["Date"]
    greatest increase[1] = Profit_Loss_Changes

Print("Greatest_Profit_Increase")

# Determine the greatest decrease in profits (date and amount) over the entire period

if (Profit_Loss_Changes < greatest decrease[1]):
    greatest decrease[0] = row["Date"]
    greatest decrease[1] = Profit_Loss_Changes
        
Print("Greatest_Profit_Decrease")

# Create summary results, print to file, and export

Pybank_Results = (
   f"\nFinancial Analysis\n"
   f"-----------------------------\n"
   f"Total Months: {Total_Months}\n"
   f"Total: ${Total_Profit_Losses}\n"
   f"Average Change: ${Average_Change}\n"
   f"Greatest Increase in Profits: {greatest increase[0]} (${greatest increase[1]}) \n"   
   f"Greatest Decrease in Profits: {greatest decrease[0]} (${greatest decrease[1]}) \n"
)


Pybank_Results = "Pybank_Results.txt"
print(Pybank_Results)
with open(Pybank_Results, "w") as file:
        file.write('Pybank_Results')