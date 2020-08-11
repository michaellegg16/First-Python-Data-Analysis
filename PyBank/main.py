# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company
# You will give a set of financial data called budget_data.csv
# The dataset is composed of two columns: Date and Profit/Losses

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results

#First import the os module to allow us to create file paths across operating systems
import os

#Import the module for reading CSV files
import csv

#Create variables and empty lists

Total_Months = 0
Total_Net_Profit = 0
Monthly_Profit_Start = 0
Monthly_Change_Cumulative = 0
Monthly_Change_List = []
Profit_Change = 0
Date_List = []

# Create relative path to access csv file

csvpath = os.path.join("Resources", "budget_data.csv")

# Open csv file and specify delimiter and a variable to hold contents
# Read the header first row

with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')  

    csv_header = next(csvreader)

# Iterate through the rows of data in order to:
# Add up the total months
# Calculate the net total of profit/loses of the entire period
# Calculate the average monthly change over the entire period
# Calculate the max/min monthly change 

    for row in csvreader:

        #Add 1 to the total months variable for each row
        Total_Months += 1

        #Add the value of profit change as in integer to the total net profit variable
        Total_Net_Profit = Total_Net_Profit + int(row[1])

        #Set the monthly profit end to the corresponding location in the data and subract the start of the month
        #Replace the monthly profit start vairable with the manthly start end variable for the next iteration
        Monthly_Profit_End = int(row[1])
        Monthly_Change = Monthly_Profit_End - Monthly_Profit_Start
        Monthly_Profit_Start = Monthly_Profit_End

        # Store this value in the empty list
        Monthly_Change_List.append(Monthly_Change)

        #Add  the profit change up
        Profit_Change += Monthly_Change

        #Find the max/min profit change
        Greatest_Monthly_Profit = max(Monthly_Change_List)
        Greatest_Monthly_Loss = min(Monthly_Change_List)

        #Add the date of each row to a list
        Date_List.append(row[0])

        #Crate a variable for the date of the max profit/loss
        Date_Of_Max_Profit = Date_List[Monthly_Change_List.index(Greatest_Monthly_Profit)]
        Date_Of_Max_Loss = Date_List[Monthly_Change_List.index(Greatest_Monthly_Loss)]


# Print the data to terminal and calculate the average monthly change.
# NOTE: All values are the same as example data except for average monthly change.
# Might have something to do with negative values of the way I am calculating then summing monthly change.
    print("FINANCIAL ANALYSIS")
    print("------------------------")
    print(f'Total Months: {Total_Months}')
    print(f'Total Net Profit: {Total_Net_Profit}')
    Average_Monthly_Change = round(Profit_Change/ len(Monthly_Change_List), 0)
    print(f'Average Monthly Change: {Average_Monthly_Change}')
    Max_Profit = max (Monthly_Change_List)
    Max_Loss = min(Monthly_Change_List)
    print(f'Max Monthly Change: {Date_Of_Max_Profit} ({Max_Profit})')
    print(f'Least Monthly Change: {Date_Of_Max_Loss} ({Max_Loss})')


# Write this data to a text file named Financial Analysis Output
with open('Financial Analysis Output.txt', 'w', newline = '') as text:
    text.write(f'FINANCIAL ANALYSIS\n')
    text.write(f'------------------------\n')
    text.write(f'Total Months: {Total_Months}\n')
    text.write(f'Total Net Profit: {Total_Net_Profit}\n')
    Average_Monthly_Change = round(sum(Monthly_Change_List)/ len(Monthly_Change_List), 0)
    text.write(f'Average Monthly Change: {Average_Monthly_Change}\n')
    Max_Profit = max (Monthly_Change_List)
    Max_Loss = min(Monthly_Change_List)
    text.write(f'Max Monthly Profit: {Date_Of_Max_Profit} ({Max_Profit})\n')
    text.write(f'Max Monthly Loss: {Date_Of_Max_Loss} ({Max_Loss})\n')