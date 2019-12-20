#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os
import csv

#The total number of votes cast
election_csv = os.path.join('.', 'Resources', 'election_data.csv')

#Lists to store data
total_votes = 0
candidates_unique = []
candidate_vote_count []
percentage = []

# Read in the CSV file
with open(election_csv) as election_file:
     # Split the data on commas
    election_data = csv.reader(election_file, delimiter=',')
    header = next(election_data)
    
    for row in election_data:
        #A complete list of candidates who received votes
        total_votes += 1

        #take value from row 2
        candidate = (row[2])

        #if already in list, index candidate and increase vote count by 1
        if candidate in candidates_unique:
                candidate_index = candidates_unique.index(candidate)
                candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        #if x not in candidates_unique, append list and increase vote count by 1
        else:
            candidates_unique.append(candidate)
            vote_count.append(1)

        percent_win = candidate_vote_count / len(total_votes) * 100


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote. 

print ("Election Results")
print("-------------------------")
print("Total Votes:", len(candidate_votes)
print("-------------------------")
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {percentage[x]}% ({candidate_vote_count[x]})')
print("-------------------------")
print("Winner:", most_votes)
print("-------------------------")
