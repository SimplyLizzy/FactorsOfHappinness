import os
import csv
csvpath = os.path.join('PyPoll','Resources','election_data.csv')
received = []
voter = [] 
candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)


    #total number of votes cast
    for row in csvreader:
        received.append(row[2])
        voter.append(row[0])
    votes = dict(zip(voter, received))
    totalVotes = len(votes)
    print(totalVotes)
    [candidates.append(name) for name in received if name not in candidates]
    frequency = {}
    for name in received:
        if name in frequency:
            frequency[name] += 1
        else:
            frequency[name] = 1
    print(frequency)
    perc = []
    for x in frequency.values():
        perc.append("{:.02%}".format((x/totalVotes)))
    print(perc)
    
    print([i for i in zip(frequency.items(), perc)])
    winner = max(frequency,key=frequency.get)
    print(winner)


# write output  
output_file = os.path.join('PyPoll','Analysis','PyPollOutput.txt')
with open(output_file, 'w') as txt_file:
    txt_file.write(f'Election Results\n-----------------------\nTotal Votes: {totalVotes}\n-----------------------\nCandidate, Votes, Percent of Total Votes:\n{[i for i in zip(frequency.items(), perc)]}\n-----------------------\n Winner:{winner}')