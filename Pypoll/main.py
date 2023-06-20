import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('..', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(election_data.csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    
# Define variables

# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

# Calculate the total number of votes cast

# Display a complete list of candidates who received votes

# Calculate the percentage of votes each candidate won

# Calculate the total number of votes each candidate won
print("")


# Calculate the winner of the election based on popular vote

print("Winner")

# Create summary results, print to file, and export

Pypoll_Results = (
   f"\nElection Results\n"
   f"-----------------------------\n"
   f"Total Votes: {Total_Votes}\n"
   f"-----------------------------\n"
   f"Total: ${Total_Profit_Losses}\n"
   f"Average Change: ${Average_Change}\n"
   f"Greatest Increase in Profits: {greatest increase[0]} (${greatest increase[1]}) \n"   
   f"Winner: \n"
)


Pybank_Results = "Pybank_Results.txt"
print(Pybank_Results)
with open(Pybank_Results, "w") as file:
        file.write('Pybank_Results')