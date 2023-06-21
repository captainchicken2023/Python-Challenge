import csv

# Path to collect data from the Resources folder
election_data = ("C:\\Users\\Junk\\Python-Challenge\\Pypoll\\Resources\\election_data.csv")

# Read in the CSV file
with open(election_data, 'r') as csvfile:

        # Define variables
        
        Total_Votes_Cast = 0
        Candidates = {}
        Candidates_Name = []
        Candidate_Results = []
        Vote_Percentage = 0
        Winner = ""
        Winning_Count = 0
        
         
        
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        #for dictionary in csvreader:
         #   Candidates_List.append(dictionary)
        
        
        #Candidates = {rows[2] for rows in csvreader}
        # Loop through the data
        for row in csvreader:
            
            # Calculate the total number of votes cast
            Total_Votes_Cast = Total_Votes_Cast + 1
            
            # Display a complete list of candidates who received votes
            # If candidate doesn't exist, add to list and count votes received
            
            #Candidates = dict({row[2]})
            #Candidates.append(row[2])
            if row[2] not in Candidates:
                Candidates[row[2]]= 1 
            else:
                Candidates[row[2]]= Candidates[row[2]] + 1 
                
            #if Candidates_Name not in Candidates_List:
                #Candidates.append(Candidates_Name)
                
            #Candidate_Results[Candidates_Name] = Candidate_Results[Candidates_Name] + 1
            
            # The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
            
            
            # Calculate the percentage of votes each candidate won
            
            # Create a list of candidates

            
            # Calculate the total number of votes each candidate won
            
            
            # Calculate the winner of the election based on popular vote
            #if final_list[candidate] > winner_votes:
               # Winning_Count = final_list[candidate]
              #  Winner = Candidates_Name
        

# Create summary results, print to file, and export

Results = (
   f"\nElection Results\n"
   f"-----------------------------\n"
   f"Total_Votes_Cast: {Total_Votes_Cast}\n"
   f"-----------------------------\n"
   f"\n{Candidates_Name} ({Vote_Percentage}%) {Candidate_Results}\n"   
   f"Winner: \n"
)

print(Candidates)
print(Results)

Pypoll_Results = "Analysis/Pypoll_Results.txt"

with open(Pypoll_Results, "w") as file:
        file.write(Results)