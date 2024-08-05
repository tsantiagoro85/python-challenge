# Import modules
import os
import csv

# Define path to dataset location
election_data_csv_path = os.path.join("Resources", "election_data.csv")

vote_count = [] # Create a list to store vote counts
candidates = [] # Create a list to store candidates

votes = len(vote_count) # Define votes

# Open dataset
with open(election_data_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",") # Read dataset as csv file
    next(csv_reader) # Read header

    # Loop through each row
    for row in csv_reader:
        votes = votes + 1 # Count votes
        candidate = row[2] # Specify candidates

        # Set if/else statement inside the for loop to determine the candidate index and then vote counts using the candidate index
        if candidate in candidates:
           candidate_index = candidates.index(candidate) # Specify the candidate index
           vote_count[candidate_index] = vote_count[candidate_index] + 1 # Determine vote count
           
        else:
           candidates.append(candidate) # Append each candidate to list candidates[]
           vote_count.append(1) # Append each vote count to list vote_count[]

# Create a list to store percentages
percentages = []

# Define majority of votes
majority_votes = vote_count[0]

# Define the index for majority of votes
majority_votes_index = 0

# Loop through each row
for count in range(len(candidates)):
    percentage = vote_count[count]/votes * 100 # Calculate percentage
    percentages.append(percentage) # Append percentage to list percentages[]
    
    # Set if/else statement inside the for loop to specify
    if vote_count[count] > majority_votes: # Specify vote counts relative to most votes
        majority_votes_index = count # Specify majority vote index
        
# Determine who is the election winner
winner = candidates[majority_votes_index]

# Determine percentages for each candidate
percentages = [round (i,2) for i in percentages]

# Print results to the terminal
print()
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {votes}")
print("--------------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print("--------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------")
 
# Write results printed in the terminal
output = os.path.join("analysis", "election_data_results.txt") # Define output path
with open(output, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes: {votes}\n")
    outfile.write("----------------------------\n")
    for count in range(len(set(candidates))):
        outfile.write(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Winner:  {winner}\n")
    outfile.write("----------------------------\n")
