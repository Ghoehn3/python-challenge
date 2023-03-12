import os
import csv

#set variables
total = 0
months = 0
greatest_increase = 0
greatest_decrease = 0
change = 0
last = 0
change_list = []
subave = 0
greatestincmonth = ""
greatestdecmonth = ""

csvpath = os.path.join(r'D:\python-challenge\PyBank\Resources\budget_data.csv')

with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
#print the total number of rows in the csv file
   # print(f"Total Months: {sum(1 for row in csvreader)}")

#print the total amount of profit/Losses
    for row in csvreader:
        #finding total
        total = total + (int(row[1]))
        months = months + 1
        #finding change by subtracting the last row from the current row
        if months >1:
            change = int(row[1])-last
            change_list.append(change) 
        #finding greatest increase and decrease
            if change > greatest_increase:
                greatest_increase = change
                greatestincmonth = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatestdecmonth = row[0]
        #finding the total change value accross all months
        last = int(row[1])
    #calculating average change
    average = sum(change_list)/len(change_list)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(months)}")
    print(f"Total: ${str(total)}")
    print(f"Average Change: $ {average:.2f}")
    print(f"Greatest Increase in Profits: {str(greatestincmonth)} (${greatest_increase})")
    print(f"Greatest Increase in Profits: {str(greatestdecmonth)} (${greatest_decrease})")


with open("PyBank.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total Months: {str(months)}", file=text_file)
    print(f"Total: ${str(total)}", file=text_file)
    print(f"Average Change: $ {average:.2f}", file=text_file)
    print(f"Greatest Increase in Profits: {str(greatestincmonth)} (${greatest_increase})", file=text_file)
    print(f"Greatest Increase in Profits: {str(greatestdecmonth)} (${greatest_decrease})", file=text_file)
  
    


   
