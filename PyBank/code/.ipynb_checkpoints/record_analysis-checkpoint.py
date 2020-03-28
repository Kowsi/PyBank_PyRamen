"""

This script for analyzing the financial records of your company

"""

# importing csv module 
import csv 
  
# csv file name 
filename = "../code/budget_data.csv"

# initializing the titles and rows list 
header = []
data = []

# initializing the data
total_months = 0
net_total_amount = 0
changes_in_pl = []
greatest_profit = 0
greatest_loss = 0

# reading csv file 
with open(filename, 'r') as csvfile:
    
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    
    # extracting header names through first row 
    header = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        amount = int(row[1])
        
        #Calculating the changes in profit 
        if data!=[]:
           changes_in_pl.append(amount-data[-1][1])
        
        data.append([row[0], amount])
        
        #calculating the net total amount of Profit/Losses over the entire period
        net_total_amount += amount
    
    # total number of months included in the dataset
    total_month = len(data)
    

#The average of the changes in Profit/Losses over the entire period
average_of_changes_PL = sum(changes_in_PL)/len(changes_in_PL)

#The greatest increase in profits (date and amount) over the entire period
greatest_profit = max(changes_in_PL)
greatest_profit_month = data[changes_in_PL.index(greatest_profit)+1][0]

#The greatest decrease in losses (date and amount) over the entire period.
greatest_loss = min(changes_in_PL)
greatest_loss_month = data[changes_in_PL.index(greatest_loss)+1][0]


output = 'Financial Analysis\n'
output += '----------------------------\n'
output += f'Total Months: {total_month}\n'
output += f'Total: ${net_total_amount}\n'
output += f'Average  Change: ${average_of_changes_PL}\n'
output += f'Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit})\n'
output += f'Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})\n'

print(output)
with open('out.txt', 'w') as f:
    print(output, file=f)
