import csv

# Path to collect data from the Resources folder
election_data = ("C:\\Users\\Junk\\Python-Challenge\\Pypoll\\Resources\\election_data.csv")

# Read in the CSV file
with open(election_data, 'r') as csvfile:

        # Define variables
        Total_Votes_Cast = 0
        Candidates = {}
        Candidate = []
        Candidate_Results = 0
        Vote_Percentage = 0
        Winner = []
        Winning_Count = 0  
        
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
    
        # Loop through the data
        for row in csvreader:
            
            # Calculate the total number of votes cast
            Total_Votes_Cast = Total_Votes_Cast + 1
            
            # Display a complete list of candidates who received votes
            # If candidate doesn't exist, add to list and count votes received
            # Save results to file
            if row[2] not in Candidates:
                
                Candidates[row[2]]= 1 
            else:
                Candidates[row[2]] = Candidates[row[2]] + 1   
                
Pypoll_Results = "Analysis/Pypoll_Results.txt"       

with open(Pypoll_Results, "w") as file:
        
    Results = (
       f"\nElection Results\n"
       f"-----------------------------\n"
       f"Total_Votes_Cast: {Total_Votes_Cast}\n"
       f"-----------------------------\n"
    )
    print(Results)
    file.write(Results)   

    # Calculate and print the percentage of votes each candidate won
    for Candidate in Candidates:
        Votes = Candidates[Candidate]
        Vote_Percentage = (Votes/Total_Votes_Cast)*100
        print(f"{Candidate}: {Vote_Percentage:.3f}% ({Votes})\n")

        file.write(f"{Candidate}: {Vote_Percentage:.3f}% ({Votes})\n")   
        
        # Calculate the winner of the election based on popular vote
        if (Votes > Winning_Count):
           Winning_Count = Votes
           Winner = Candidate

# Complete summary results, print to file, and export
    print(f"Winner: {Winner}")
    file.write(f"Winner: {Winner}")




