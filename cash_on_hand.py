from pathlib import Path
import re, csv
file_path=Path.cwd()/"project_group"
file_path_Cash_on_hand_csv=Path.cwd()/"csv_reports"/"Cash on hand.csv"
file_path_Cash_on_hand_csv.touch()
empty_list=[]
with file_path_Cash_on_hand_csv.open(mode="r",encoding="UTF-8",newline="") as file:
  reader = csv.reader(file)
  next(reader)
  for line in reader:
    empty_list.append({"Day": line[0],"Cash On Hand": line[1]})
    
print(empty_list) 
         


