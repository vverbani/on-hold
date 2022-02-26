# Project imports
import os
import sys
import pandas as pd
import numpy as np

# Copy final `csv` file into `xlsx` as it's easier to look at and for users to edit later on
def copy_to_excel(input_file, output_file):
    # Reading the csv file
    df_new = pd.read_csv(WRITE_CSV_FILE)
    # saving xlsx file
    GFG = pd.ExcelWriter(WRITE_XLSX_FILE)
    df_new.to_excel(GFG, index = False)
    GFG.save()
    return output_file

# TO-DO: Create ENV vars for these - add logic so the items don't have to exist under `./src/`
# Initialize global vars
READ_FILE= "./src/files/on-hold.csv"
WRITE_CSV_FILE= "./src/files/output.csv"
WRITE_XLSX_FILE= "./src/files/output.xlsx"
line_count= 0

# Filter per region: EMEA Support, APAC Support, Customer Support or US Support
REGION_FILTER= "US Support"

# These are the headers and their respective values we want
file_headers= [ 'Group' ]

# Handle logic to see if the output files exist in directory - create if they don't. Error out if original flight isn't in the directory
if(os.path.exists(READ_FILE) != True): sys.exit("You don't have the original excel file, please import it before moving on.")
if(os.path.exists(WRITE_CSV_FILE) != True): open(WRITE_CSV_FILE, 'a').close()
if(os.path.exists(WRITE_XLSX_FILE) != True): open(WRITE_XLSX_FILE, 'a').close()

input_file= pd.read_csv(READ_FILE)

# TO-DO: Add coloumns;
## `Colour Code` -> this will identify the urgency of the ticket

# Write to both a `.csv` and a `xlsx` file
output_file= input_file[file_headers]
output_file.to_csv(WRITE_CSV_FILE, index=False)

for row in output_file:
    if row[0] != REGION_FILTER:
        print(row)

# Filter by region
# https://note.nkmk.me/en/python-pandas-drop/ useful link

# Also save to an excel file
copy_to_excel(WRITE_CSV_FILE, WRITE_XLSX_FILE)