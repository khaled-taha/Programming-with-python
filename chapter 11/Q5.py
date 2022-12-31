"""
5. Repeatedly ask the user to enter a team name and the how many games the team won and
how many they lost. Store this information in a dictionary where the keys are the team names
and the values are lists of the form [wins, losses].

(a) Using the dictionary created above, allow the user to enter a team name and print out
the team's winning percentage.
(b) Using the dictionary, create a list whose entries are the number of wins of each team.
(c) Using the dictionary, create a list of all those teams that have winning records.
"""
teams = {}

while True:
    team_name = input('Enter the team name: ')
    if team_name == '':
        break
    wins = eval(input('Enter the games that this team won: '))
    losses = eval(input('Enter the games that this team lost: '))
    teams[team_name] = [wins, losses]

# a)
team_name = input('Enter the team name: ')
winning_percentage = ( teams[team_name][0] / (teams[team_name][0] + teams[team_name][1]) ) * 100
print(team_name, " : ", winning_percentage)

# b)
wins = [win[0] for win in teams.values()]
print(wins)

# c)
teams_win = wins = [team for team in teams if teams[team][0] > 0]
print(teams_win)