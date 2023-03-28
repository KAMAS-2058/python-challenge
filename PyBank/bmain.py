#importing csv file from resources
import csv
import os.path

with open("Resources/budget_data.csv", newline='') as budcsv:
    infocsv = csv.reader(budcsv, delimiter=',')
    header = next(infocsv)

    date=[]
    gainloss=[]
    prolos = 0
    roundone=0
    total=0
    averagec=0
    v1 = 0
    v1_line1 = 0
    v2 = 0
    v2_line2 = 0

    #setting up the lists & getting number of months
    for row in infocsv:
        date.append(row[0])
        gainloss.append(int(row[1]))
        
        datec = len(date)

    for roundone in range(datec):
        total = total+int(gainloss[roundone])

    for roundtwo in range(datec-1):
        averagec = averagec+(float(gainloss[roundtwo+1])-float(gainloss[roundtwo]))

        changem = (float(gainloss[roundtwo+1]) - float(gainloss[roundtwo]))
        if changem> v1:
            v1 = changem
            v1_line1 = roundtwo
        else:
            v1=v1

        if changem<v2:
            v2 = changem    
            v2_line2 = roundtwo
        else:
            v2 = v2

analysis = f'\
------------------------\n\
Financial Analysis\n\
Total Months: {datec}\n\
Total: ${total}\n\
Average Change: ${round(averagec/(datec-1)),2}\n\
Greatest Increase in Profits: {date[v1_line1 + 1]} (${int(v1)})\n\
Greatest Decrease in Profits: {date[v2_line2 + 1]} (${int(v2)})\n'

print(analysis)


Analysisfile = open("analysis","pybank.txt","w")
Analysisfile.writelines(analysis)
Analysisfile.close()
 