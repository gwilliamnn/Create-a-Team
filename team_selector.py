#!/usr/bin/env python3

import random

def insert_player_names():
	
	while True:
	
		name = input("## Enter the name of the player\n## And press ENTER: ")

		if name == "q":
			break
		
		players.append(name)
		
		print(f"==> {name} has been added\n")
		print(f" - We have {len(players)} player(s) in the list\n")
		
		user_type_decision = input(f"## To add more player  -  Type.: 1\n## To check the list   -  Type.: 2\n## To go for next step -  Type.: 3\n###################### -  Enter: ")
		
		user_type_decision = int(user_type_decision)
		
#		print(user_type_decision)
		
#		if user_type_decision == 1:
		
		if user_type_decision == 2:
			print("")
			for lst in players:
				print(f"=> {lst}")
			print("")
			
			user_type_decision_2 = input(f"## To add more player  -  Type.: 1\n## To remove a player  -  Type.: 2\n## To go for next step -  Type.: 3\n###################### -  Enter: ")
			
			user_type_decision_2 = int(user_type_decision_2)
				
			if int(user_type_decision_2) == 2:
				
				player_to_remove = input("Type the name of the player do you want to remove: ")
				
				players.remove(player_to_remove)
				
				print(f"{player_to_remove} removed, the new list is: ")
				
				for lst in players:
					print(f"=> {lst}")
			
			if int(user_type_decision_2) == 3:
				
				break
				
			
		if user_type_decision == 3:
			break
		
	return players

players = []

insert_player_names()
print(players)

#print("Welcome to Team/Player Allocator \n")
#
#name_or_number = input("Do you want put the names of the players? \n Enter y or n")
#	if name_or_number.lower() == "y":
#
#many_players = input("How many players will play?\n Enter the number of players: ")
#
## Change the names bellow if you want. Please keep the "". You can add more names, just use , "Name" (comma, space double quote mark).
#players = []
#
## Chose Team or Player
#
#team_or_ind = input("Is it a team or individual sport? \
#              \nType team or individual: ")
#print("")
#
#if team_or_ind.lower() == "team":
#
#	while True:
#	
#		random.shuffle(players)
#		team1 = players[:len(players) // 2]
#		team_cap = random.choice(team1)
#		print(f"Team 1 captain is:\n => {team_cap.upper()}")
#		print("Team 1 players: ")
#		for player in team1:
#			if player == team_cap:
#				print(f">> {player.upper()} (C)")
#				
#			else:
#					print(f"> {player}")
#		print("\n")
#			
#		team2 = players[len(players) // 2:]
#		team_cap = random.choice(team2)
#		print(f"Team 2 captain is:\n => {team_cap.upper()}")
#		print("Team 2 players: ")
#		for player in team2:
#			if player == team_cap:
#				print(f">> {player.upper()} (C)")
#				
#			else:
#					print(f"> {player}")
#		
#		response = input(f"Pick teams ? Type y or n: ")
#		
#		if response == "n":
#			break
#	
#	print("\nlet's Play Then!")
#	
#else:
#	for i in range(0, 20, 2):
#		
#		print(f"{players[i]} vs {players[i + 1]}")
#		
#		start = random.randrange(i, i+2)
#		print(players[start] + " starts\n")