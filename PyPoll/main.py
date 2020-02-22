# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Import the os module to allow us to create file paths across operating systems
# Import the csv module for reading csv files
import os
import csv

# Create variables and empty lists
Total_Votes = 0
Candidates = []
Complete_Candidate_List = []
Count_Of_Votes = []
Vote_Percentages = []

# Create a relative path to access the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the csv file and specify the delimiter and a variable to hold its contents
# Read the header first row

with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

# Iterate through the rows to add up the total amount of votes and fill the candidates list 

    for row in csvreader:
        Total_Votes += 1
        Candidates.append(row[2])

# Create a set from the candiate list and iterate through the set

    for candidate in set(Candidates):

        # Add each new candidate to a list 
        Complete_Candidate_List.append(candidate)

        # Count the amount of votes for each candidate
        Vote_Count = Candidates.count(candidate)
        Count_Of_Votes.append(Vote_Count)

        # Calculate a percentage of the amount of votes and store that in the list
        Vote_Percent = round(((Vote_Count/Total_Votes) * 100), 2)
        Vote_Percent = str(Vote_Percent)
        Vote_Percentages.append(Vote_Percent)
    
    # Find the max amount of votes for a candidate and delcare them the winner
    Most_Votes = max(Count_Of_Votes)
    Election_Winner = Complete_Candidate_List[Count_Of_Votes.index(Most_Votes)]

# Print this data to the terminal
print(f'VOTING ANALYSIS')
print(f'-----------------')
print(f'Total Votes: {Total_Votes}')
print(f'Candidates: {Complete_Candidate_List}')
# A for loop iterates a new print function for each candidate in order to print their data on new lines
for candidate in range(len(Complete_Candidate_List)):
    print(f'{Complete_Candidate_List[candidate]}: {Vote_Percentages[candidate]}% with {Count_Of_Votes[candidate]} votes.')
print(f'THE WINNER IS: {Election_Winner}!')

# Write this data to a text file named Election Data Output
with open('Election Data Output.txt', 'w', newline = '') as text:
    text.write(f'ELECTION DATA ANALYSIS\n')
    text.write(f'--------------------------\n')
    text.write(f'Total Votes: {Total_Votes}\n')
    text.write(f'Candidates: {Complete_Candidate_List}\n')
    for candidate in range(len(Complete_Candidate_List)):
        text.write(f'{Complete_Candidate_List[candidate]}: {Vote_Percentages[candidate]}% with {Count_Of_Votes[candidate]} votes.\n')
    text.write(f'THE WINNER IS: {Election_Winner}\n')