
import os
import csv
csvpath = 'C:\\python-challenge\\PyBank\\Resources\\budget_data.csv'
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    countmonths = 0
    total = 0
    change = 0
    totalchange = 0
    previoustotal = 0
    initialchange = 0
    greatest = 0
    lowest = 0
    for row in csvreader:
        countmonths = countmonths + 1
        total = total + int(row[1])
        if greatest<int(row[1]):
            greatest=int(row[1])
            profmonth = row[0]
        if lowest>int(row[1]):
            lowest=int(row[1])
            lossmonth = row[0]
        if countmonths == 1:
            initialchange = int(row[1])
        if countmonths == 2:
            totalchange = totalchange + (int(row[1]) - initialchange)
            previoustotal = int(row[1])
        if countmonths>2:
            totalchange = totalchange + (int(row[1]) - previoustotal)
            previoustotal = int(row[1])
    total
    average = round(totalchange/(countmonths-1),2)
    
    str1=("Total Months: "+ str(countmonths))
    str2=("Total: $" + str(total))
    str3=("Average Change: "+ str(average))
    str4=("Greatest Profit: $" + str(greatest) + " in " + str(profmonth))
    str5=("Greatest Loss: $" + str(lowest) + " in " + str(lossmonth))
    
    textlist = [str1, str2, str3, str4, str4]
    for line in textlist:
        print(line)
       
    output_file = 'C:\\python-challenge\\PyBank\\analysis\\ProfitLoss_analysis.txt'
    
    with open (output_file, "w", newline="\n") as datafile:
        for line in textlist:
            datafile.write(line)
            datafile.write("\n")
        datafile.close()
        