"""
Take the same data as was for previous problem (i.e.,Voting_results.py). You
have to take your data, split to 4 sets by the following rule: Take the first 3 sets
same size, last set alone is allowed to have an excess of upto 3 data items.
For today’s assignment this data is to be interpreted differently as results of
throwing a die repeatedly by 4 different players called W,X,Y and Z.
• A −→ 1,B −→ 2,...,F −→ 6.
• Other letters are invalid throws, they are counted in the attempts.
• The score for the player is the sum of numbers obtained in their throws.
• For each player the target score is 50.
Your task: Identify the player who is the fastest to reach the target and say how
many throws she needed to achieve it, and also give total score for each of the 4
players. (If there is a tie all the winner’s name should be announced)
"""

data = "CCCDDABFQCCDDABEQCCCDABEFCCCDABEFCCCDAABFQCCDDABEQCCDDABEQCCCDABEFCCCDABEFCCCDDABFQCCDDABEQCCCDABEFCCCDABEFCCCDAAEFZCCDDABEQCCDDABEQCCCDABEFCCCDABEFCCCDAABFQCCDDABEQCCCDABEFCCCDABEFCCCDABEFZCCDDABEQCCDDABEQCCCDABEFCCCDABEFCCCDAABFQCCDDABEQCCCDABEFCCCDABEFCCCDABEFZCCDDABFQCCDDABEQCCCDABEFCCCDABEFCCCDAABFQCCDDABEQCCCDABEQCCCDABEFCCCDABEF"
#slicing the give data into required no. of sets
n = 4  #no. of sets to be made
length = len(data)//n
remain = len(data)%n

score_data = []
for score in range(n):
    p = data[score*length:(score+1)*length]
    score_data.append(p)
    
# adding the remaining string values in the last set
if remain != 0:
    for score in range(remain,0,-1):
        extra = data[-score]
        score_data[n-1] += extra
        
#defining a function which assigns weight to the string values according to number appearing on a dice
def letter_weights(letter):
    if letter == 'A':
        return 1
    elif letter == 'B':
        return 2
    elif letter == 'C':
        return 3
    elif letter == 'D':
        return 4
    elif letter == 'E':
        return 5
    elif letter == 'F':
        return 6
    else:
        return 0
    
#calculating total score of each player
players = ["W","X","Y","Z"]
weights = []
for k in range(n):
    score_vals = [letter_weights(score) for score in score_data[k]]
    weights.append(score_vals)
    print("Total score of",players[k],": ",sum(score_vals), "&","Invalid scores are",score_vals.count(0))

#checking the no. of throws made by each player to cross a minimum of 50
target = 50
scores = [0]*n
throws = []
for i in range(len(scores)):
    for j in range(len(weights[-1])):
        scores[i] = scores[i] + weights[i][j] 
        if scores[i] >= target:
            throws.append(j+1)
            break
            
print()
player_throws = list(zip(throws,players))
print("Total throws taken by each player until target score are: ",player_throws)

#results are printed considering if two(or more) players have same no. of throws
min_throw = min(throws)
for index in range(len(player_throws)):
    if player_throws[index][0] == min_throw:
        print(player_throws[index][1],"is the winner, taking a minimum of",min_throw,"throws.")
        

