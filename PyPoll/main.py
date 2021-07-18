        #PyPoll Challenge

#import dependencies
import csv, os

#import file as variable
csv_file = os.path.join("Resources", "election_data.csv")

#set path for output file
my_report = open("analysis/myreport.txt", "w")

#access file and set variable
with open(csv_file) as profLoss:

    #read file, set variable for file reader
    file = csv.reader(profLoss)

    #skip and store the header
    header = next(file)
    
    #set variables
    votes = 0

    pervoteKhan = 0

    pervoteCorrey = 0

    pervoteLi = 0

    pervoteOtooley = 0

    voteKhan = 0

    voteCorrey = 0

    voteLi = 0

    voteOtooley = 0

    #set empty list for the winner
    winner = ()

    #loop through rows
    for row in file:

        #track total votes
        votes += 1

        #track individual votes for candidates
        if row[2] == "Khan":
            voteKhan += 1

        elif row[2] == "Correy":
            voteCorrey += 1

        elif row[2] == "Li":
            voteLi += 1

        elif row[2] == "O'Tooley":
            voteOtooley += 1

    #calculate percent of votes
    pervoteKhan = voteKhan/votes*100

    pervoteCorrey = voteCorrey/votes*100

    pervoteLi = voteLi/votes*100

    pervoteOtooley = voteOtooley/votes*100

    #set list for candidates
    canlist = [voteKhan, voteOtooley, voteLi, voteCorrey]

    #find the winner
    maxvote = max(canlist)

    if maxvote == voteKhan:
        winner = "Khan"

    elif maxvote == voteCorrey:
        winner = "Correy"

    elif maxvote == voteLi:
        winner = "Li"

    elif maxvote == voteOtooley:
        winner = "O'Tooley"

    output = f'''
    Election Results
  -------------------------
  Total Votes: {votes:,}
  -------------------------
  Khan: {pervoteKhan:,.3f}% ({voteKhan:,})
  Correy: {pervoteCorrey:,.3f}% ({voteCorrey:,})
  Li: {pervoteLi:,.3f}% ({voteLi:,})
  O'Tooley: {pervoteOtooley:,.3f}% ({voteOtooley:,})
  -------------------------
  Winner: {winner}
  -------------------------
    
    '''   

    #print results
    print(output)

#write to file
my_report.write(output)