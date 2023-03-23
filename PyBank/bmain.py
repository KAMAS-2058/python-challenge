#importing csv file from resources
import csv

with open("Resources/budget_data.csv", newline='') as budcsv:
    infocsv = csv.reader(budcsv, delimiter=',')
    header = next(infocsv)

    date=[]
    gains=[]

#number of months in the csvfile
    for row in infocsv:
        date.append(row[0])
        monthnum = len(date)

        gains.append(row[1])
    print(gains)
    #print(monthnum)

    



