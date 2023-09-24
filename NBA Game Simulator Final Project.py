'''Project: NBA series simulation
Name: Jory Peters
Description: This code simulates an NBA series and prints the results into another file
'''
import random
# The class for the Teams
class Teams:
    def __init__(self, team_name):
        self.team_name = team_name

    def __str__(self):
        return f"{self.team_name}"

# The Sub Class
class Players(Teams):
    def __init__(self, name, jersey_number):
        super().__init__("Warriors")
        self.name = name
        self.jersey_number = jersey_number

    def __str__(self):
        return f"Player Name: {self.name}, Jersey Number: {self.jersey_number}"
#records three stats for pts, rebs, and assists.
class Game:
    def __init__(self, point, rebound, assist): # Adding these to each player
        self.point = point
        self.assist = assist
        self.rebound = rebound
#These stats are for display
    def get_stats(self):
        return f"Points: {self.point}, Rebounds: {self.rebound}, Assists: {self.assist}"


# The Players of team 1
team1 = Teams("WARRIORS")
w_player1 = Players("Stephen Curry", 30)  # Name and Jersey Number
w_player2 = Players("Klay Thompson", 11)
w_player3 = Players("Andrew Wiggins", 22)
w_player4 = Players("Draymond Grenn", 6)
w_player5 = Players("Jordan Poole", 3)


# The Players of team 2
team2 = Teams("76ERS")
s_player1 = Players("Joel Embiid", 21) # Name and Jersey Number
s_player2 = Players("James Harden", 1)
s_player3 = Players("PJ Tucker", 17)
s_player4 = Players("Tyrese Maxey", 0)
s_player5 = Players("Tobias Harris", 12)

# Loop to simulate multiple games
f=open("FinalScoreNStats.txt", "w")
num_games = int(input("How many games do you want to simulate? "))
team1series = 0
team2series = 0
for game_num in range(1, num_games+1):

    # Randomize player stats
    w_player1_game = Game(random.randint(10, 50), random.randint(0, 10), random.randint(0, 7))
    w_player2_game = Game(random.randint(5, 40), random.randint(0, 6), random.randint(0, 5))
    w_player3_game = Game(random.randint(0, 18), random.randint(0, 3), random.randint(0, 6))
    w_player4_game = Game(random.randint(0, 10), random.randint(0, 7), random.randint(0, 8))
    w_player5_game = Game(random.randint(0, 21), random.randint(0, 5), random.randint(0, 3))

    s_player1_game = Game(random.randint(10, 50), random.randint(0, 20), random.randint(0, 5))
    s_player2_game = Game(random.randint(5, 50), random.randint(0, 20), random.randint(0, 10))
    s_player3_game = Game(random.randint(0, 7), random.randint(0, 4), random.randint(0, 5))
    s_player4_game = Game(random.randint(0, 30), random.randint(0, 4), random.randint(0, 4))
    s_player5_game = Game(random.randint(0, 14), random.randint(0, 6), random.randint(0, 4))
    
    #this will show the best stats from the star player
    f.write(f"{team1}\n")
    f.write(f"{w_player1}\n")
    f.write(f"{w_player1_game.get_stats()}\n")
    #same thing but for the other team
    f.write(f"{team2}\n")
    f.write(f"{s_player1}\n")
    f.write(f"{s_player1_game.get_stats()}\n")
# Adding up the players amount of points together to get the final score
    team1_score = w_player1_game.point + w_player2_game.point + w_player3_game.point + w_player4_game.point + w_player5_game.point
    team2_score = s_player1_game.point + s_player2_game.point + s_player3_game.point + s_player4_game.point + s_player5_game.point
 # Deciding who takes the game in the series
    if team1_score > team2_score:
        final = (f"Game {game_num}: goes to {team1} \n")
        f.write(final)
        team1series +=1
    else:
        final = (f"Game {game_num}: goes to {team2} \n")
        f.write(final)
        team2series +=1
# Calculating which team won more games to win the series
if team1series > team2series:
    winner = (f"{team1} win the championship with {team1series} games")
elif team2series > team1series:
    winner = (f"{team2} win the championship with {team2series} games")
else:
    winner = (f"This is a tied matchup...")
f.write(winner)
f.close()






