import random

lst = ['rock', 'paper' , 'scissor']
player_winning_combo = [['rock', 'scissor'],['paper', 'rock'],['scissor', 'paper']]
match_combo = []
player_pick = input("Enter your choice:").lower()
match_combo.append(player_pick)

com_pick = random.choice(lst)
match_combo.append(com_pick)
if player_pick == com_pick:
	print("both picked the same thing")
else:
	print(f"computer picked {com_pick}") 
	if match_combo in player_winning_combo:
		print(f"{player_pick} beats {com_pick}. Player wins.")
	else:
		print(f"{com_pick} beats {player_pick}. Computer wins.")
