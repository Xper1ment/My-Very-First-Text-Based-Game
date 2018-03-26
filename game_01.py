'''My Very First Text Based Game'''


def start_adventure():
	options=["A Stone","A Bottle","A Jungle","A Sign Board"]
	print("You See:")
	for num,opt in enumerate(options,start=1):
		print("{}:{}".format(num,opt))
	player_decision=int(input("Choose an option:"))
	if player_decision in (1,2):
		player_resources.extend(options[player_decision-1])
		print("You have accquired {}".format(options[player_decision-1]))
		options.pop(player_decision-1)
	elif player_decision == 4:
		print("The Sign Board reads \"This is the forbidden island of an unnamed goddes. Anyone who sets foot on this island will suffer the wrath of the mad TITAN\""
	elif player_decision == 3:
		print("You went deep into the Jungle")
	else:
		print("WRONG INPUT!!!TRY AGAIN!!!")


player_name=input("Please Enter Player Name -> ")
player_resources=[]
print("You are on a deserted island.You need to get off that island. In Order to do that, you need to gather supplies available on the island. Press the number assosciated with the option in order to acess them")
start_adventure()