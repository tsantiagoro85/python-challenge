# Import modules
import os
import csv

budget_data_csv_path = os.path.join("Resources", "budget_data.csv") # Define path to dataset location

months = [] # Create a list for months
profit = [] # Create a list for profit

count_months = len(profit) # Define the total number of months
total = sum(profit) # Define the total profits and losses

with open(budget_data_csv_path) as csvfile: # Open dataset as csv file
    csv_reader = csv.reader(csvfile, delimiter = ",") # Read dataset as csv file
    csv_header = next(csvfile) # Read header

    for row in csv_reader:  # Loop through each row
        count_months = count_months + 1 # Count months
        current_month = int(row[1]) # Specify the current month of profits and losses
        total = total + current_month # Specify the total profits and losses amount
        
        # Set and if/else statement inside the for loop to determine the profit loss for previous and current months, and profit loss change
        if (count_months == 1):
            previous_month = current_month  # Make the value of previous month to be equal to current month
        
        else:
            months.append(row[0]) # Append each month to list months[]
            profit_change = current_month - previous_month # Compute change in profit loss
            profit.append(profit_change) # Append each profit_change to the profit[]
            previous_month = current_month # Make the current_month to be previous_month
           
    average_profit = round(sum(profit)/(count_months - 1), 2) # Determine average of profits and losses

    greatest_increase = max(profit) # Determine greatest increase in profits and losses
    greatest_decrease = min(profit) # Determine greatest in profits and losses

    greatest_increase_month = months[profit.index(greatest_increase)] # Determine month of greatest increase
    greatest_decrease_month= months[profit.index(greatest_decrease)] # Determine month of greatest decrease

# Print the analysis results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_profit}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses: {greatest_decrease_month} (${greatest_decrease})")

# Write a text file with the results printed in the terminal
output = os.path.join("analysis", "budget_data_results.txt")
with open(output, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {count_months}\n")
    outfile.write(f"Total: ${total}\n")
    outfile.write(f"Average Change: ${average_profit}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses: {greatest_decrease_month} (${greatest_decrease})\n")
