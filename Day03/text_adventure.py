# Day 3 - Text Adventure Game | Control Flow and logic operators

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
cross_road = input("Type 'left' or 'right'\n").lower()
if cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    swim_or_wait = input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if swim_or_wait == "wait":
        print("You arrive at island unharmed. There is a house with 3 doors")
        pick_door = input("One red, one yellow, and one blue. Which color do you choose?\n").lower()
        if pick_door == "red":
            print("You are attacked by a wild Charizard and burned by its fire. Game Over")
        elif pick_door == "blue":
            print("You are attacked by a wild Kyogre and faint. Game Over.")
        elif pick_door == "yellow":
            print("You found the Raichunite X to evolve your Raichu! You Win!")
        else:
            print("You are attacked by Team Rocket. Game Over.")
    else:
        print("You get attacked by a wild Gyarados. Game Over.")
else:
    print("You fell into a hole. Game Over. ")
