import math
import copy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def winner_loser(a_id,a,b_id,b):
    rules=[['C','P'],
    ['P','R'],
    ['R','L'],
    ['L','S'],
    ['S','C'],
    ['C','L'],
    ['L','P'],
    ['P','S'],
    ['S','R'],
    ['R','C']]
    if [a,b] in rules:
        return a_id,b_id
    elif a==b:
        return min(a_id,b_id),max(a_id,b_id)
    return b_id,a_id
n = int(input("Enter number of players: "))
players=[]
print("Enter player ID's, followed by chosen signs\n")
for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    players.append([numplayer,signplayer])
#print(players)

round_winners=copy.deepcopy(players)
matches=[]

for i in range(int(math.log(n,2))):
    j=0
    length=len(round_winners)
    while j<length:
        player_1_id, player_1_sign=round_winners[j][0], round_winners[j][1]
        player_2_id, player_2_sign=round_winners[j+1][0], round_winners[j+1][1]
        win,lose=winner_loser(player_1_id,player_1_sign,player_2_id,player_2_sign)
        #print(win,lose)
        matches.append([win,lose])
        for x in round_winners:
            if lose==x[0]:
                round_winners.remove(x)
        j+=1
        length=len(round_winners)    
    #print(round_winners)

final_winner=round_winners[0][0]
#print(matches)
print("WINNER: Player "+str(final_winner))

winner_matches=""
for x in matches:
    if final_winner==x[0]:
        winner_matches=winner_matches+str(x[1])+" "
print("Matches against Players: "+winner_matches.rstrip())