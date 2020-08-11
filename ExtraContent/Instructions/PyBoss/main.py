#Import the OS Module
import os

#Import CSV
import csv

#Import Pandas
import pandas as pd 

    #STATES
    #Copy/paste state dictionary from online
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

EmpIDList = []
FirstNameList = []
LastNameList =[]
DOBList = []
SSNList = []
StateList = []

csvpath = os.path.join("ExtraContent", "Instructions", "PyBoss", "employee_data.csv")

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

        #Append dates to initial list
        DOBList.append(row[2])

        #Append SSN to initial list
        SSNList.append(row[3])

        #Grab the state abbreviation from the dictionary and store it in a variable
        StateAbbr = us_state_abbrev[row[4]]

        #Store the abbreviated values in the list
        StateList.append(StateAbbr)

    #DATE CONVERSION
    import datetime

    #Create an empty list for the convert date values
    ConvDateList = []

    #Loop through the DOBList and format the date as desired
    for date in DOBList:
        NewDate = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%m/%d/%Y")
        ConvDateList.append(NewDate)

    #Create an empty list for the hidden SSN
    HiddenSSNList = []

    #Loop through the SSNList and hide the first 5 characters
    for ssn in SSNList:
        HiddenSSN = "***-**-" + str(ssn[7:11])
        HiddenSSNList.append(HiddenSSN)


    #print(StateList)