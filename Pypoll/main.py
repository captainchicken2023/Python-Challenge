import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('..', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(election_data.csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    


# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

# Calculate the total number of votes cast

# Display a complete list of candidates who received votes

# Calculate the percentage of votes each candidate won

# Calculate the total number of votes each candidate won
print("")


# Calculate the winner of the election based on popular vote

print("Winner")