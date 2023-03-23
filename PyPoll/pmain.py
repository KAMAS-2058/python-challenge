import csv

with open("resources/election_data.csv") as electdata:
    electreader = csv.reader(electdata, delimiter=',')
    header = next(electreader)
    

    bid =[]
    county =[]
    candidate = []
    votec = 0
    who = 0

    for row in electreader:
        bid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    balcount = int(len(bid))
    
    canname =[]       
    canname.append(candidate[0])

    for who in range(balcount):
        if candidate[who+1] != candidate[who] and candidate[who+1] not in canname:
            canname.append(candidate[who+1])

    n = len(canname)

