#Import the OS Module
import os

#Import CSV
import csv

#Import Pandas
import pandas as pd 

EmpIDList = []
FirstNameList = []
LastNameList =[]
DOBList = []
SSNList = []
StateList = []

csvpath = os.path.join("Instructions", "PyBoss", "employee_data.csv")

with open(csvpath, newline = '') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')  

    csv_header = next(csvreader)

    for row in csvreader:

        EmpIDList.append(row[0])
        #Make sure there are no duplicates by converting the List into a Dictionary!
        EmpIDDict = list(dict.fromkeys(EmpIDList))

        #Split the names into FirstName and LastName
        #Make sure to store the split names intoa variable! The split values need a list to hold them before appending to their respective lists
        FullNames = row[1]
        FullNameList = FullNames.split()

        #Append the first and last names to their respective lists
        FirstNameList.append(FullNameList[0])
        LastNameList.append(FullNameList[1])

    print(LastNameList)
