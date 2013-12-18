import csv
import itertools

# Mention the file location of the csv file
# Read the file in 2 different readers (one can be used to create a list of data and the other to find the number of columns in the file)
# For Unix, 'rU' mode can be used.
reader1, reader2 = itertools.tee(csv.reader(open('company_data.csv','rU')))

## Find number of coulmns
num_cols = len(next(reader1))-1
del reader1

data = list(reader2)

## Find number of rows
num_rows = (sum(1 for row in data)) -1

#To start with the first company listed i.e 2
start_company = 2

#List of company with their corresponding highest shares
best_company = []

## Loop through each company
while start_company <= (num_cols):

    #Reset the start_row and highest_share for each company
    start_row = 1
    highest_share = start_row

    ## Loop through each row
    while start_row <= num_rows:
        #Comapre the highest share stored with the value of the share from the current row
        if int(data[highest_share][start_company]) <= int(data[start_row][start_company]):
            highest_share = start_row

        #Go to the next row
        start_row += 1

    # Best Company = Company Name + year + month + value
    best_company.append(str(data[0][start_company])+": "+str(data[highest_share][0]) +", "+str(data[highest_share][1])+" : "+str(data[highest_share][start_company]))
    # Go to next company
    start_company +=1

# Display the final list
for item in best_company :
    print item
