"""

This script for analyzing the financial records of your company

"""

# importing csv module 
import csv 
  
# csv file name 
menu_filename = "../Resources/menu_data.csv"
sales_filename = "../Resources/sales_data.csv"

# initializing the titles and rows list 
header = []
menu_data = {}
sales_data = []


# reading menu_data csv file 
with open(menu_filename, 'r') as csvfile:
    
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    
    # extracting header names through first row 
    header = next(csvreader) 

    # extracting each data row one by one 
    for row in csvreader: 
        menu_data[row[0]] = [row[1], row[2], row[3],row[4]]



# reading sale_data csv file 
with open(sales_filename, 'r') as csvfile:
    
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    
    # extracting header names through first row 
    header = next(csvreader) 

    # extracting each data row one by one 
    for row in csvreader: 
        sales_data.append([row[0], row[1], row[2], row[3], row[4]])


# Initialize an empty report dictionary to hold the future aggregated per-product results
report = {}

# Loop through every row in the sales data
for sale in sales_data:
    
    quantity = int(sale[3])
    sales_item = sale[4]
    
    # Initialize the product report entry to 0 if not already in the dictionary
    if report.get(sales_item)==None:
        report[sales_item] = {"01-count": 0, 
                              "02-revenue": 0, 
                              "03-cogs": 0, 
                              "04-profit": 0}
    
    # Get the menu_data details for the sale_item
    menu = menu_data[sales_item]
    
    # If sale item present in the menu_data, calculate the sale item's report
    if menu!=None:
        price = float(menu[2])
        cost = float(menu[3])
        profit = quantity * (price - cost) 
        report[sales_item]["01-count"] += quantity
        report[sales_item]["02-revenue"] += price * quantity
        report[sales_item]["03-cogs"] += cost * quantity
        report[sales_item]["04-profit"] += profit * quantity
    else:
        print(f'{sales_item} does not contains data')


# Print the aggregated product report
for sales_item in report:
    print(f'{sales_item} : {report[sales_item]}')

