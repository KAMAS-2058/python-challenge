import csv

with open("resources/election_data.csv") as electdata:
    electreader = csv.reader(electdata, delimiter=',')
    header = next(electreader)
    

    bid =[]
    county =[]
    candidate = []
    votec = 0

    for row in electreader:
        bid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])


    bid_count = len(bid)
    for votec in range(bid_count):
        votec = votec + (int[bid_count])
        print(votec)
