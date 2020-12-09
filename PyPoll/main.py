import os
import csv
csvpath = 'C:\\python-challenge\\PyPoll\\Resources\\election_data.csv'
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    countvotes = 0
    candvotes = 0
    pctvotes = []
    votes = []
    candidates = []
    mostvotes = 0
    for row in csvreader:
        countvotes = countvotes + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            votes.append(0)
            pctvotes.append(0)
        if candidate in candidates:
            index = candidates.index(row[2])
            candvotes = votes[index]
            candvotes = candvotes + 1
            votes[index] = candvotes
    for i in range(len(pctvotes)):
        pctvotes[i] = round((votes[i]/countvotes)*100,3)
    for j in range(len(pctvotes)):
        if mostvotes < pctvotes[j]:
            mostvotes = pctvotes[j]
            winner = candidates[j]
    
    print("Election Results")
    print("--------------------")
    print("Total Votes: "+str(countvotes))
    print("--------------------")
    for k in range(len(candidates)):
        print(candidates[k] + ": " + str(pctvotes[k]) + "% ("+str(votes[k])+")")
    print("--------------------")
    print("Winner: "+winner)
    print("--------------------")

    output_file = 'C:\\python-challenge\\PyPoll\\analysis\\ElectionResults_analysis.txt'

    with open (output_file, "w", newline="\n") as datafile:
        datafile.write("Election Results")
        datafile.write("\n")
        datafile.write("\n")
        datafile.write("Total Votes: "+str(countvotes))
        datafile.write("\n")
        datafile.write("--------------------")
        datafile.write("\n")
        for k in range(len(candidates)):
            datafile.write(candidates[k] + ": " + str(pctvotes[k]) + "% ("+str(votes[k])+")")
            datafile.write("\n")
        datafile.write("--------------------")
        datafile.write("\n")
        datafile.write("\n")
        datafile.write("Winner: "+winner)
        datafile.close()
        
        