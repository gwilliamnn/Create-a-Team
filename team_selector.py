#!/usr/bin/env python3

import random

# Change the names bellow if you want. Please keep the "". You can add more names, just use , "Name" (comma, space double quote mark).
players = [
	"Christi"  , "Camille" , "Emmanuel" , 
	"Cecelia"  , "Delores" , "Becky" , 
	"Hubert"   , "Aimee"   , "Van" , 
	"Wallace"  , "Annette" , "Darrell" , 
	"Salvador" , "Wilson"  , "Dianne" , 
	"Jody"     , "Jen"     , "Victor" , 
	"Evelyn"   , "Wayne"
]

print("Welcome to Team/Player Allocator \n")

# Chose Team or Player

team_or_ind = input("Is it a team or individual sport? \
               \nType team or individual: ")
print("")

if team_or_ind.lower() == "team":

	while True:
	
		random.shuffle(players)
		team1 = players[:len(players) // 2]
		team_cap = random.choice(team1)
		print(f"Team 1 captain is:\n => {team_cap.upper()}")
		print("Team 1 players: ")
		for player in team1:
			if player == team_cap:
				print(f">> {player.upper()} (C)")
				
			else:
					print(f"> {player}")
		print("\n")
			
		team2 = players[len(players) // 2:]
		team_cap = random.choice(team2)
		print(f"Team 2 captain is:\n => {team_cap.upper()}")
		print("Team 2 players: ")
		for player in team2:
			if player == team_cap:
				print(f">> {player.upper()} (C)")
				
			else:
					print(f"> {player}")
		
		response = input(f"Pick teams again? Type y or n: ")
		
		if response == "n":
			break
	
	print("\nlet's Play Then!")
	
else:
	for i in range(0, 20, 2):
		
		print(f"{players[i]} vs {players[i + 1]}")
		
		start = random.randrange(i, i+2)
		print(players[start] + " starts\n")