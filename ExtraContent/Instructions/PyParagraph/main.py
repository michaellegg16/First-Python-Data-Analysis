#Import the OS Module
import os

#Import CSV
import csv

#Import Pandas
import pandas as pd 

# Import re
import re

# Set path for file
rawData = 'python-challenge/ExtraContent/Instructions/PyParagraph/raw_data/paragraph_2.txt'

# Open the TXT file
with open(rawData, newline= "") as txtfile:
    
    # Read the file and store it in a variable
    text = txtfile.read()

    # Determine the amount of words using the split function
    wordList = text.split(" ")
    words = len(wordList)

    # Determine the amount of sentences
    sentences = len((re.split("(?<=[.!?])", text)))

    # Determine the amount of letters in the paragraph
    letters = len(text)

    # Determine the average sentence length
    avgLength = words / (sentences)

    # Print the results
    print(f'There are {words} words in the paragraph.')
    print(f'There are {sentences} sentences in the paragraph.')
    print(f'There are {letters} letters in the paragraph.')
    print(f'The average sentence length is {avgLength} words.')