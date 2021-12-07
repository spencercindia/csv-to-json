# "OrderDate","Region","City","Category","Product","Quantity","UnitPrice","TotalPrice"

import json
import csv
# file_path = 'C:\Users\spenc\Documents\sampledatafoodsales.csv'

with open('C:\\Users\\spenc\\Documents\\sampledatafoodsales.csv', 'r') as csvfile:
    
    csv_dict_reader = csv.DictReader(csvfile)

    data = {'rows': []}
    for row in csv_dict_reader:
        data['rows'].append(row)
    # print(data)

with open('babiesfirst.json', 'w') as csvfile:
    json.dump(data, csvfile, indent=4)
