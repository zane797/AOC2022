# Open the Data File
from _ast import If
import os
from setuptools.command.build_ext import if_dl

def text():
    # Get file name
    filename = input("What is the full name of the data file? ")
    
    # Change CWD to the directory of the file
    os.chdir('AOC2022')
    
    # Open file and save it as Data
    textdata = open(filename, "r")
    data = textdata.readlines()

    # Close the text file
    textdata.close()

    # Remove the \n's from data to get only the original rows from the txt file.
    i = 0
    while i < len(data):
        data[i] = data[i].replace('\n', '')
        i = i + 1
    i = 0

    return data

def init():
    
    # Establish Local Variables
    data = []
    choice = ''

    # Allow for test inputs
    choice = input('Would you like to enter "test" mode or "standard" mode: ')

    # Load in Data
    if choice == 'standard': data = text()

    if choice == 'test':
        data.append(input('Enter a single test string: '))

    return data