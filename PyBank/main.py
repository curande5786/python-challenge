           #PyBank Challenge

#import dependencies
import csv, os

#import file as variable
csv_file = os.path.join("Resources", "budget_data.csv")

#set path for output file
my_report = open("analysis/myreport.txt","w")

#access file and set variable
with open(csv_file) as profLoss:

    #read file, set variable for file reader
    file = csv.reader(profLoss)

    #skip and store the header
    header = next(file)

    #set variables
    total = 0

    months = 0

    first = 0

    prevrow = 0

    prev_rev = 0

    ch_sum = 0

    #set arrays to track date of and values for 
    #greatest increase and decrease in profit
    inc = ['',0]

    dec = ['',0]

    #begin looping rows
    for row in file:

        #track total months counted in data
        months += 1

        #set variable to the value in column 2
        rev = int(row[1])

        #count total revenue
        total += rev

        #track changes from row to row
        change = rev - prev_rev

        #run conditional setting the change to zero on the first row
        if prev_rev == 0:
            change = 0

        #add tracked changes together
        ch_sum += change

        #set variable to current row before moving on to the next one
        prev_rev = rev

        #find greatest increase in profit
        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change

        #find greatest decrease in profit
        if change < dec[1]:
            dec[0] = row[0]
            dec[1] = change

    #set variable containing the results
    output = f'''
      Financial Analysis
  ----------------------------
  Total Months: {months}
  Total: ${total:,}
  Average  Change: ${ch_sum/(months-1):,.2f}
  Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
  Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
  '''

    #print results
    print(output)

#write to file
my_report.write(output)