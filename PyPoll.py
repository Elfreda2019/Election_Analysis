import os
import csv

# assign a variable to the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#creating a filename variable to the direct or in direct path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

# read the file object with the reader function
    file_reader = csv.reader(election_data)
    

    # printing header row
    headers = next(file_reader)
    print(headers)



        



# 1. The data we need to retrieve.
# 2. The total number of votes cast
# 3. A complete list of candidates who received votes
# 4. The total number of votes esh candidate won
# 5. The winner of the election based on popular votes