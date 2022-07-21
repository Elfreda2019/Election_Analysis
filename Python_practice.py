from ast import If


counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

for county in counties:
    print(county)

# making a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438 }
print(counties_dict)

for counti in counties_dict:
    print(counti)


# looping through the dictionary
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters. ")

# making a list of dictionary
voting_data = [ {"county": "Arapahoe", "registered voters": 422829}, 
                {"county": "Denver", "registered voters": 463353}, 
                {"county": "Jefferson", "registered voters": 432438} ]
# print(voting_data)

for county_dict in voting_data:
    print(county_dict.values()) 


# uisng range function on list of dictionary to print values
for i in range(len(voting_data)):
    print (voting_data[i]['county'])



# import os
# import csv

# assign a variable to the file to load and the path
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     print(election_data)

#creating a filename variable to the direct or in direct path to the file
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# using the open() function with the "w" mode we will write data to the file
#outfile = open(file_to_load, "w")

# write to the file
# outfile.write("hello world")

#using the open statement to open a text file
# with open(file_to_save, "w") as txt_file:   

    #write to the file

    # txt_file.write("Counties in the Election ")

    # txt_file.write("\n-----------------------")

    # txt_file.write("\nArapahoe\nDenver\nJefferson ")







# 1. The data we need to retrieve.
# 2. The total number of votes cast
# 3. A complete list of candidates who received votes
# 4. The total number of votes esh candidate won
# 5. The winner of the election based on popular votes