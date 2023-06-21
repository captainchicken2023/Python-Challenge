import csv

# Path to collect data from the Resources folder
election_data = ("C:\\Users\\Junk\\Python-Challenge\\Pypoll\\Resources\\election_data.csv")

# Read in the CSV file
with open(election_data, 'r') as csvfile:

        # Define variables
        
        Total_Votes_Cast = 0
        Candidates = {}
        Candidates_Name = []
        Candidate_Results = 0
        Vote_Percentage = 0
        Winner = []
        Winning_Count = 0  
        
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        
        #Candidates = {rows[2] for rows in csvreader}
        # Loop through the data
        for row in csvreader:
            
            # Calculate the total number of votes cast
            Total_Votes_Cast = Total_Votes_Cast + 1
            
            # Display a complete list of candidates who received votes
            # If candidate doesn't exist, add to list and count votes received
            if row[2] not in Candidates:
                
                Candidates[row[2]]= 1 
                
            else:
                Candidates[row[2]] = Candidates[row[2]] + 1            

            # Calculate the percentage of votes each candidate won
            for Candidates[row[2]] in Candidates_Name:
                Vote_Percentage = (Candidates[row[2]]/Total_Votes_Cast)*100
               
            # Calculate the winner of the election based on popular vote
            if (Candidate_Results > Winning_Count):
               Winning_Count = Candidate_Results
               Winner = Candidates_Name
        

# Create summary results, print to file, and export

Results = (
   f"\nElection Results\n"
   f"-----------------------------\n"
   f"Total_Votes_Cast: {Total_Votes_Cast}\n"
   f"-----------------------------\n"
   f"\n{Candidates}\n"   
   f"Winner: \n"
)

print(Results)


Pypoll_Results = "Analysis/Pypoll_Results.txt"

with open(Pypoll_Results, "w") as file:
        file.write(Results)