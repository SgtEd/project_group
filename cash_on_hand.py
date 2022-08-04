from pathlib import Path
import re, csv
import glob

from decimal import Decimal

def readCSV(exchange_data):

    """

This function is to find the cash deficit using the csv file "Cash on Hand". 

    """


    arr = []

    prevDay = 0
    prevAmount = 0

    currDay = 0
    currAmount = 0

    print("Finding cash deficit..")

    with open("csv_reports/Cash on hand.csv") as csv_file:
        csv_reader =  csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 1:

                currDay = row[0]

                # convert current amount to SGD
                # USD/exchange_data = SGD
                currAmount = Decimal(row[1]) / exchange_data
                currAmount = round(currAmount, 2)



            if line_count > 1:

                prevDay = currDay
                prevAmount = currAmount

                currDay = row[0]

                # USD/exchange_date = SGD
                currAmount = Decimal(row[1]) / exchange_data 
                currAmount = round(currAmount, 2)

                if currAmount < prevAmount:
                    amountDiff = prevAmount - currAmount

                    # print ("Hi")
                    entry = [currDay, float(amountDiff)]
                    arr.append(entry)

            line_count += 1
            # print(line_count)
        
        # print(arr)

    return arr

