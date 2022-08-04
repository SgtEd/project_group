from itertools import count
from pathlib import Path
import re, csv
file_path=Path.cwd()/"project_group"
file_path_Cash_on_hand_csv=Path.cwd()/"csv_reports"/"overheads.csv"
file_path_Cash_on_hand_csv.touch()
empty_list=[] 
empty_list_expenses=[]
empty_list_category=[]
empty_list_1=[]
with file_path_Cash_on_hand_csv.open(mode="r",encoding="UTF-8",newline="") as file:
    reader = csv.reader(file)
    next(reader)
#    for line in reader:
#        #print(line[1])
#        empty_list.append({"category": line[0],"Overheads": line[1]})
#        empty_list=line
#        empty_list_expenses=[empty_list[1]]           
#        empty_list_expenses.append(float(empty_list[1]))
#        empty_list_expenses=float(empty_list_expenses)
#print(empty_list_1)
#highest_expense=max(empty_list_expenses)
#print(highest_expense)
#print(empty_list)
#highest_expenses=max(line)
#print(highest_expenses)

#with file_path_Cash_on_hand_csv.open(mode="r",encoding="UTF-8",newline="") as file:
#    reader = csv.reader(file)
#    next(reader)
#    #for line in reader:
#    #    for value in line:
#    #        empty_list.append(value)
#    #        
##print(empty_list)   
##empty_list.sort(reverse=False)
##print(empty_list)
    for line in reader:
        empty_list=line
        for value in empty_list:
            empty_list_1.append(empty_list)
        
            #empty_list.append(value)
            #empty_list_expenses=[empty_list[1]]
            
            empty_list_expenses.append(float(empty_list[1]))
            highest_expense=max(empty_list_expenses)
            highest_expense=float(highest_expense)
            category=line[0]
            
            for count, num in enumerate(empty_list):
                print(category,num)
                if num == highest_expense:
                    break
            
                




#
#
            #empty_list.append({empty_list[0]:empty_list[1]})
            #empty_list=sorted(empty_list)
            #empty_list_category=[empty_list[0]]
            #empty_list_overheads=[empty_list[1]]
            #print(empty_list_overheads)
        #for value in line:
        #    #highest_overheads=empty_list_overheads
        #    empty_list_overheads.append(value)
#print(empty_list_overheads)
        #    empty_list_overheads=empty_list_category
        #    break
        #print(empty_list_category)
    