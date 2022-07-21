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
