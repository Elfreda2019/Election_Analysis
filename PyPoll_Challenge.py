import os
import csv

# assign a variable to the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#creating a filename variable to the direct or in direct path to the file
file_to_save = os.path.join("analysis", "election_results.txt")

#Intialize a total vote counter
total_votes = 0

#candidate option
candidate_options = []

#county option
county_options = []

# candidate votes
candidate_votes = {}

# county votes
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Winning county
winning_county = ""
winning_county_count = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

# read the file object with the reader function
    file_reader = csv.reader(election_data)
    

    # printing header row
    headers = next(file_reader)

    # print each row in the csv file
    for row in file_reader:
        # Add to the total votes count
        total_votes += 1


        #candidate name from each row
        candidate_name = row[2]

        # # add the candidate name to the candidate list
        # candidate_options.append(candidate_name)

        # if candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # add it to the list of candidates
            candidate_options.append(candidate_name)

            # tracking the candidate's votes count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate count
        candidate_votes[candidate_name] += 1

    
        # county name from each row
        county_name = row[1]

        # if county does not match any existing county
        if county_name not in county_options:
            
            # add it to the list of county
            county_options.append(county_name)

            # tracking the county votes count
            county_votes[county_name] = 0

             # add to county count
        county_votes[county_name] += 1
    


# save the results to our test file

with open(file_to_save, "w") as txt_file:
    # print the final vote to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

# Determine the percentage of county votes for each candidate by looping through the counts.
    # iterate through the county list
    for county_name in county_votes:


        # Retrieve vote count of a county.
        num_votes = county_votes[county_name]

        # Calculate the percentage of num_votes.
        county_vote_percentage = float(num_votes) / float(total_votes) * 100

        # Print the county name and percentage of votes.
       
        # print out each county name, vote count, and percentage of votes to terminal
        
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({num_votes:,})\n")

        print(county_results)

        # Save the candidate results to our text file.
        txt_file.write(county_results)
    

        # Determine winning vote count and candidate
        # Determine if the votes are greater then the winning count.
        if (num_votes > winning_county_count):

           # if true  theb set winning_count  = votes and winning_percent = vote_percentage
            winning_county_count = num_votes

            # set the winning_candidate equal to the candidate's name
            winning_county = county_name

    winning_county_summary = (
        f"---------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"---------------------------\n")

    print(winning_county_summary)

  # save the winning county name to the text file.
    txt_file.write(winning_county_summary)
 
    # Determine the percentage of votes for each candidate by looping through the counts.
    # iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage}% of the votes.")
   
        # print out each candidate's name, vote count, and percentage of votes to terminal
        
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
    

        # Determine winning vote count and candidate
        # Determine if the votes are greater then the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

           # if true  then set winning_count  = votes and winning_percent = vote_percentage
            winning_count = votes

            winning_percentage = vote_percentage

            # set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Votes Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    
    print(winning_candidate_summary)

    # save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)