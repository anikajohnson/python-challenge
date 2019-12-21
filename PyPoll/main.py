#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os
import csv

#The total number of votes cast
election_csv = os.path.join('.', 'Resources', 'election_data.csv')

#Lists to store data
total_votes = 0
candidates_unique = []
candidate_vote_count = []


# Read in the CSV file
with open(election_csv) as election_file:
    election_data = csv.reader(election_file, delimiter=',')
    header = next(election_data)
    
    for row in election_data:
        #A complete list of candidates who received votes, count rows
        total_votes += 1

        #take candidate from row 2
        candidate = (row[2])

        #if already in list, take index of candidate and increase vote count by 1
        if candidate in candidates_unique:
                candidate_index = candidates_unique.index(candidate)
                candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        #if x not in candidates_unique, append list and increase vote count by 1
        else:
            candidates_unique.append(candidate)
            candidate_vote_count.append(1)



percent = []
max_votes = candidate_vote_count [0]
max_index = 0

#The percentage of votes each candidate won
#The total number of votes each candidate won
for x in range(len(candidates_unique)):
    vote_percent = round(candidate_vote_count[x]/total_votes*100, 2)
    percent.append(vote_percent)

    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

#The winner of the election based on popular vote. 
winner = candidates_unique[max_index]

#print results to terminal
print ("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {percent[x]}% ({candidate_vote_count[x]})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

#print to file
output_file = os.path.join("election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write ("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write("-------------------------\n")
    for x in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[x]} : {percent[x]}% ({candidate_vote_count[x]})\n')
    datafile.write("-------------------------\n")
    datafile.write(f'Winner: {winner}\n')
    datafile.write("-------------------------\n")