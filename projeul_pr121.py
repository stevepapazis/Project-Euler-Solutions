problem = """\
Problem 121: Disc game prize fund

A bag contains one red disc and one blue disc. In a game of chance a player
takes a disc at random and its colour is noted. After each turn the disc is
returned to the bag, an extra red disc is added, and another disc is taken
at random.

The player pays £1 to play and wins if they have taken more blue discs than
red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is
exactly 11/120, and so the maximum prize fund the banker should allocate for
winning in this game would be £10 before they would expect to incur a loss.
Note that any payout will be a whole number of pounds and also includes the
original £1 paid to play the game, so in the example given the player actually
wins £9.

Find the maximum prize fund that should be allocated to a single game in which
fifteen turns are played.\n\n"""

#Use some simple probability theory to understand the code.

from fractions import *

def probability_to_get_blue_disk_in_turn(n): return Fraction(1,n+1)

#N is the number of turns of the game

def probability_player_wins_game_in(N):
    l = [[]]
    
    for depth in range(N,0,-1):
        temp = []
        for i in l:
            temp.append(i+[1]) # player got blue disk
            temp.append(i+[-1]) # player got red disk
        l = temp.copy()

    outcomesWhenPlayerWins = filter(lambda x: sum(x)>0, l)
    
    probability = 0

    for i in outcomesWhenPlayerWins:
        p = Fraction(1,1)
        for j in range(0, N):
            if i[j]==1: p*= probability_to_get_blue_disk_in_turn(j+1)
            else: p*= 1-probability_to_get_blue_disk_in_turn(j+1)
        probability += p

    return probability

#The expected lose of the game organiser in a game with N turns is:
#E(L) = 1-probability_player_wins_game_in(N)-payout*probability_player_wins_game_in(N)

#Let p = probability_player_wins_game_in(N).
# E(L)>0 <=> 1 - p - (1-payout)*p > 0
#        <=> 1/p > payout 
#The game organiser will lose money if they offer a prize greater than 1/p.
#Therefor, the maximum prize must be the greater integer less than 1/p.

print(problem,"Answer: £",int(1/probability_player_wins_game_in(15)), sep="")
