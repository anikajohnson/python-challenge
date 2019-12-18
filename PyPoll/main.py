#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os
import csv

#The total number of votes cast
election_csv = os.path.join('.', 'Resources', 'election_data.csv')

#Lists to store data
voter_id = []
county = []
candidate_votes = []

varibles
Khan_count = 0
Correy_count = 0
Li_count = 0
# Read in the CSV file
with open(election_csv) as election_file:
     # Split the data on commas
    election_data = csv.reader(election_file, delimiter=',')

    header = next(election_data)
    for row in election_data:
    #A complete list of candidates who received votes
        voter_id.append(row[0])
        county.append(row[1])
        candidate_votes.append(row[2])

    def unique(candidate_votes):
        candidate_list = []

        for x in candidate_votes:
            if x not in candidate_list:
                candidate_list.append(x)
        for x in candidate_list:
           print (x, end=" ")

print(unique(candidate_votes))

    for row in election_data:
        if "Khan" == candidate_votes:


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.