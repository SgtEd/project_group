from itertools import count
from pathlib import Path
import re, csv

from decimal import Decimal
file_path=Path.cwd()/"project_group"
file_path_Cash_on_hand_csv=Path.cwd()/"csv_reports"/"overheads.csv"
file_path_Cash_on_hand_csv.touch()

def readCSV(exchange_data): 
    """
    this function is to find the highest overheads using the overheads.csv
    
    """

    arr = []

    highest = 0 
    highestCategory = ""

    print("Finding highest overheads..")

    #opens csv file
    with open('csv_reports/overheads.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
    

        for row in csv_reader:

            # start from where the actual values appear
            # skip the header
            if line_count > 0:

                # convert currency
                convertedAmount = Decimal(row[1]) / exchange_data
                # round off to 2 decimal places
                roundedAmount = round(convertedAmount , 2)

                # find the highest
                if roundedAmount > highest:
                    highest = roundedAmount
                    highestCategory = row[0]

            # go through each line
            line_count +=1 

    return [highestCategory, highest]
            
