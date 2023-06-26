import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join("..", "Pybank", "Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Define variables
    Total_Months = 1
    Month_Changed = []
    Previous_Change = 0
    Profit_Loss_Changes = 0 
    Profit_Loss_Changes_list = []
    Greatest_Profit_Increase = ["", 0]
    Greatest_Profit_Decrease = ["", 999999999999999999999999999999]
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    firstrow = next(csvreader)

    # Loop through the data
    Total_Profit_Losses = int(firstrow[1])
    Previous_Change = int(firstrow[1])
    for row in csvreader:
    
        # Determine the total number of months in the data set
        Total_Months = Total_Months + 1
        
        # Calculate the net total amount of "Profit/Losses" over the entire period
        Total_Profit_Losses = Total_Profit_Losses + (int(row[1]))
        
        # Calculate the changes in "Profit/Losses" over the entire period
        Profit_Loss_Changes = int(row[1]) - Previous_Change
        Previous_Change = int(row[1])
        Profit_Loss_Changes_list = Profit_Loss_Changes_list + [Profit_Loss_Changes]
        Month_Changed = Month_Changed + [row[0]]
    
        # Determine the greatest increase in profits (date and amount) over the entire period
        if (Profit_Loss_Changes > Greatest_Profit_Increase[1]): 
            Greatest_Profit_Increase[0] = row[0]
            Greatest_Profit_Increase[1] = Profit_Loss_Changes
        
        # Determine the greatest decrease in profits (date and amount) over the entire period
        if (Profit_Loss_Changes < Greatest_Profit_Decrease[1]):
            Greatest_Profit_Decrease[0] = row[0]
            Greatest_Profit_Decrease[1] = Profit_Loss_Changes

# Calculate average change
Average_Change = round(sum(Profit_Loss_Changes_list) / len(Profit_Loss_Changes_list), 2)

# Create summary results, print to file, and export
Analysis = (
   f"\nFinancial Analysis\n"
   f"-----------------------------\n"
   f"Total Months: {Total_Months}\n"
   f"Total: ${Total_Profit_Losses}\n"
   f"Average Change: ${Average_Change}\n"
   f"Greatest Increase in Profits: {Greatest_Profit_Increase[0]} (${Greatest_Profit_Increase[1]}) \n"   
   f"Greatest Decrease in Profits: {Greatest_Profit_Decrease[0]} (${Greatest_Profit_Decrease[1]}) \n"
)

print(Analysis)

Pybank_Results = "Analysis/Pybank_Results.txt"

with open(Pybank_Results, "w") as file:
        file.write(Analysis)