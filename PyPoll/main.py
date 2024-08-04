# Import modules
import os
import csv

election_data_csv_path = os.path.join("Resources", "election_data.csv") # Define path to dataset location

vote_count = [] # Create a list to store vote counts
candidates = [] # Create a list to store candidates

votes = len(candidates) # Define votes

with open(election_data_csv_path) as csvfile: # Open dataset as csv file
    csv_reader = csv.reader(csvfile, delimiter = ",") # Read dataset as csv file
    next(csv_reader) # Read header

    for row in csv_reader: # Loop through each row
        votes = votes + 1 # Count votes
        candidate = row[2] # Specify candidates

        # Set if/else statement inside the for loop to determine the candidate index and the vote counts
        if candidate in candidates:
           candidate_index = candidates.index(candidate) # Specify the candidate index
           vote_count[candidate_index] = vote_count[candidate_index] + 1 # Determine vote count
           
        else:
           candidates.append(candidate) # Append each candidate to candidates list
           vote_count.append(1) # Append each vote count

percentages = [] # Create a list to store percentages
majority_votes = vote_count[0] # Define majority of votes
majority_votes_index = 0 # Define the index for majority of votes

for count in range(len(candidates)):
    percentage = vote_count[count]/votes * 100
    percentages.append(percentage)
    if vote_count[count] > majority_votes:
        print(majority_votes)
        majority_votes_index = count
        
winner = candidates[majority_votes_index] # Define election winner
percentages = [round (i,2) for i in percentages] # Determine percentages

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
