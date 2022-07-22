# Election_Analysis

## Overview of Election Audit
We are assisting a Colorado Board of Election employee in an elction audit of the tabulated results for the US congretional precint in Colorado.

We are using python for this audit analysis in order to use the code to automate other election results.


## Election-Audit Results
- The total number of votes cast in the congretional election was 369,711.
- The election took place in 3 counties and their name, percentage of votes and  number of votes are as follows respectively:
    
    - Jefferson: 10.5% (38,855)
     
    - Denver: 82.8% (306,055)
       
    - Arapahoe: 6.7% (24,801)

- Denver happens to be the county with the highest number of vote turnout.
- 3 candidates took part in the election and the number of votes as well as their percentages are as follow.

   - Charles Casper Stockham: 23.0% of the votes and 85,213 number of votes.
   
   - Diana DeGette 73.8% of the votes and 272,892 number of votes.
 
   - Raymon Anthony Doane: 3.1% of the votes and 11,606 number of votes.

Diana DeGette, won the elections with 727,892 votes.


## Election Audit Summary
The script for the analysis can be used for any election analysis. Depending on which colomn the variable you want to analyse are, you can edit the script changing the number 2 in the code below for instance to the index of the variable in the data as shown in the sample code below:

        for row in file_reader
        total_votes += 1
        candidate_name = row[2]
        

Also you need to update the name election_results.csv to the name of the file where your csv data is stored in order to get the path right as shown in the sample code below:

     file_to_load = os.path.join("Resources", "election_results.csv")

            
