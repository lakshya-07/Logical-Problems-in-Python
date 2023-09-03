"""
This is a problem of declaring election results given all the voting data. 
The data consists of  a string, and each character represents one vote. 
We assume the candidates in the election are named A, B, …, Z (exactly 26 candidates).

The program counts how many A’s how many B’s etc and declare the winner based on which letter is occurring maximum. 
We will allow small letters and capital letters to  represent vote for the same candidate.

If any other character is present it is to be interpreted as an invalid vote.
"""



votes_data = "CCCCDDABFMCCCDDABEMCCCDDABEFCCCCDABEFCCCCDDABFMCCCDDABEMCCCDDABEFCCCCDABEFCCCCDAABFMCCCDDABEMCCCDDABEFCCCCDABEFCCCCDAABFMCCCDDABEMCCCDDABEFCCCCDABEFCCCCDAABFMCCCDDABEMCCCDDABEFCCCCDABEFCCCCDAABFMCCCDDABEMCCCDDABEFCCCDDABEFCCCCDAAEFZCCCDDABEMCCCDDABEMCCCDDABEFCCCCDABEFZCCCDDABEMCCCDDABEMCCCDDABEFCCCCDABEFZCCCDDABEMCCCDDABEMCCCDDABEFCCCCDABEFZCCCDDABFMCCCDDABEMCCCDDABEFCCCCDABEF"

votes_data.upper()
candidates = [0]*26    #only A,B,C,D,E,F are eligible
invalid_votes = 0

for vote in votes_data:
    position = ord(vote)-65
    if position >= 0 and position <= ord("F")-65:
        candidates[position] += 1
    else:
        invalid_votes += 1
        
for i in range(6):
    print("Votes of candidate",chr(i+65)," = ",candidates[i])
    
#for finding the winner
max_votes = max(candidates)    
winner = candidates.index(max_votes)
        
print("Winner is",chr(winner +65),"- receiving",max_votes,"votes out of",len(votes_data))

#for finding the runner up and margin of victory we throw away winner votes
candidates[winner] = 0
runner_up_votes = max(candidates)

runner_up = candidates.index(runner_up_votes)

print("Runner up is",chr(runner_up +65),"- receiving",runner_up_votes,"votes out of",len(votes_data))
margin = max_votes - runner_up_votes
print("Margin of victory is",margin)
print("Total invalid votes are ",invalid_votes)
