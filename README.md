# Rock-Paper-Scissors-Spock-Lizard-tournament
Problem Statement:
An international Rock Paper Scissors Lizard Spock tournament is 
organized, all players receive a number when they register.

Each player chooses a sign that he will keep throughout the tournament among:
Rock (R)
Paper (P)
sCissors (C)
Lizard (L)
Spock (S)

Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors
and in case of a tie, the player with the lowest number wins (it's scandalous but it's
the rule).

INPUT: Line 1: an integer N representing the number of participants in the competition
Lines 2 to N+1: an integer NUMPLAYER indicating the player number (players have 
distinct numbers between 1 and N) followed by a letter 'R', 'P', 'C', 'L' or 'S' 
indicating the chosen sign SIGNPLAYER

OUTPUT: Line 1: the number of the winner
	Line 2: the list of its opponents separated by spaces

Eg.: 

Input:
8
4 R
1 P
8 P
3 R
7 C
5 S
6 L
2 L

Output:
WINNER: Player 2
Matches against Players: 6 5 1
