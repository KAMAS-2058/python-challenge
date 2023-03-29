import csv

with open("resources/election_data.csv") as electdata:
    electreader = csv.reader(electdata, delimiter=',')
    header = next(electreader)
    
    bid =[]
    county =[]
    candidate = []
    votec = 0
    #wholoop = 0
    options =[]

    #assigning the columns
    for row in electreader:
            bid.append(row[0])
            county.append(row[1])
            candidate.append(row[2])

    #making a count of the voter ids
    balcount = int(len(bid))
    #print(balcount)

#finding the available candidates that received votes
for element in candidate:
    if element not in options:
        options.append(element)







  

    

    
    

    # canname =[]       
    # canname.append(candidate[1])

    # for who in range(balcount):
    #     if candidate[who+1] != candidate[who] and candidate[who+1] not in canname:
    #         canname.append(candidate[who+1])

    # n = len(canname)
    # print(n)
