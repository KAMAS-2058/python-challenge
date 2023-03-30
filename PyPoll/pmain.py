import csv

with open("resources/election_data.csv") as electdata:
    electreader = csv.reader(electdata, delimiter=',')
    header = next(electreader)
    
    bid =[]
    county =[]
    candidate = []
    options =[]
    

    #assigning the columns
    for row in electreader:
            bid.append(row[0])
            county.append(row[1])
            candidate.append(row[2])

    #making a count of the voter ids
    balcount = int(len(bid))

#finding the available candidates that received votes
for element in candidate:
    if element not in options:
        options.append(element)

# options_two = options
#options list ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']

#finding the number of votes each candidate got
optint = len(options) #made options an integer for the loops
vote_per_can = []

for canvote in range(optint):
     vote_per_can.append(candidate.count(options[canvote]))

# vote_per_can_two = vote_per_can

pertcan = []

#finding the percentage each candidate got
for canper in range(optint):
     pertcan.append(vote_per_can[canper]/balcount)

# pertcan_two = pertcan
#finding a winner loop
winvotes = 0

#finding the winner of the election
for winloop in range(optint):
     if vote_per_can[winloop]>winvotes:
        winner = options[winloop]
        winvotes = vote_per_can[winloop]

#making the win percentage readable
pertcan_format = ['%.2f' % elem for elem in pertcan]

#using list() to make a zip that is printable
# percentage_for_candidates = list(pertcan_format)
# available_candidates = list(options)
# votes_for_each_candidate = list(vote_per_can)
# results = zip(available_candidates,percentage_for_candidates,votes_for_each_candidate)

# print(options_two)
# print(vote_per_can_two)
# print(pertcan_format)
# print(winner)
# print(winvotes)


ElectionResults = f'\
Election Results!!\n\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\
Total Turnout of: {balcount}\n\
The Election Results!:\n\
{options}\n\
{vote_per_can}\n\
{pertcan_format}\n\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\
Congratulations {winner}\n\
With {winvotes} Votes!!!'

print(ElectionResults)

Analysisp = open("Analysisp/pypoll.txt","w")
Analysisp.writelines(ElectionResults)
Analysisp.close()
    
