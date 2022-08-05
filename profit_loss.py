
from pathlib import Path
import re, csv
import glob

from decimal import Decimal

def readCSV(exchange_data):
    """
    This function is to find the profit deflict using profit-and-loss-usd.csv file

    """

    arr = []

    prevDay = 0
    prevAmount = 0

    currDay = 0
    currAmount = 0

    print("Finding profit deficit..")

    # opens csv file
    with open('csv_reports/profit-and-loss-usd.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0


        for row in csv_reader:

            if line_count == 1:
                
                currDay = row[0]
                currAmount = Decimal(row[4]) / exchange_data 
                currAmount = round(currAmount, 2)

            if line_count > 1:

                prevDay = currDay
                prevAmount = currAmount

                currDay = row[0]
                
                # convert currency 
                # USD/exchange_data = SGD
                currAmount = Decimal(row[4]) / exchange_data
                currAmount = round(currAmount, 2)
                

                if currAmount < prevAmount:
                    amountDiff = prevAmount - currAmount

                    entry = [currDay, float(amountDiff)]
                    arr.append(entry)

            
            # go through each line
            line_count += 1

        # print(arr)    
    
    return arr


 
        
