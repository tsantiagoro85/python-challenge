# Import modules
import os
import csv

# Define path to dataset location
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Initialize variables
months = [] # Create a list for months
profit = [] # Create a list for profit

count_months = len(months) # Define the total number of months
total = sum(profit) # Define the total profits and losses

# Open dataset
with open(budget_data_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",") # Read dataset as csv file
    csv_header = next(csvfile) # Read header

    # Loop through each row
    for row in csv_reader:
        count_months = count_months + 1 # Count months
        current_month = int(row[1]) # Define current month
        total = total + current_month # Determine the total profits and losses amount
        
        # Set an if/else statement inside the for loop to determine the profits for previous and current months, and profit loss change
        if (count_months == 1):
            previous_month = current_month  # Make the value of previous month to be equal to current month
        
        else:
            months.append(row[0]) # Append each month to list months[]
            profit_change = current_month - previous_month # Determine the profit change
            profit.append(profit_change) # Append each profit_change to list profit[]
            previous_month = current_month # Make the current_month to be previous_month
           
    # Determine average profit
    average_profit = round(sum(profit)/(count_months - 1), 2)

    # Determine greatest increase and greatest decrease in profit
    greatest_increase = max(profit)
    greatest_decrease = min(profit)

    # Determine month of greatest increase and greatest decrease in profit
    greatest_increase_month = months[profit.index(greatest_increase)]
    greatest_decrease_month= months[profit.index(greatest_decrease)]

# Print the analysis results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_profit}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses: {greatest_decrease_month} (${greatest_decrease})")

# Write file with the results printed to the terminal
output = os.path.join("analysis", "budget_data_results.txt")
with open(output, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {count_months}\n")
    outfile.write(f"Total: ${total}\n")
    outfile.write(f"Average Change: ${average_profit}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses: {greatest_decrease_month} (${greatest_decrease})\n")
