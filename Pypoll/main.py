import csv

# Path to collect data from the Resources folder
election_data = ("C:\\Users\\Junk\\Python-Challenge\\Pypoll\\Resources\\election_data.csv")

# Read in the CSV file
with open(election_data, 'r') as csvfile:

        # Define variables
        
        Total_Votes_Cast = 0
        Candidates = []
        Candidate_Results = {}
        Vote_Percentage = 0
        Winner = ""
        Winning_Count = 0
        
         
        
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        
        # Loop through the data
        for row in csvreader:
            
            # Calculate the total number of votes cast
            Total_Votes_Cast = Total_Votes_Cast + 1
            
            # Display a complete list of candidates who received votes
            Candidates = row[2]
            

            # The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
            
            
            # Calculate the percentage of votes each candidate won
            
            # Create a list of candidates
            Candidates = [
            "Tom Cruise",
            "Angelina Jolie",
            "Kristen Stewart",
            "Denzel Washington"]
            
            # Calculate the total number of votes each candidate won
            
            
            # Calculate the winner of the election based on popular vote
        
        

# Create summary results, print to file, and export

Results = (
   f"\nElection Results\n"
   f"-----------------------------\n"
   f"Total_Votes_Cast: {Total_Votes_Cast}\n"
   f"-----------------------------\n"
   f"{Candidates[2]} ({Vote_Percentage}%) {Candidate_Results}\n"   
   f"Winner: \n"
)


print(Results)

Pypoll_Results = "Analysis/Pypoll_Results.txt"

with open(Pypoll_Results, "w") as file:
        file.write(Results)