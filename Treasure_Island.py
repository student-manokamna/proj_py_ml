
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
********************************************************************************
''')
# copy anything above images from the internet https://ascii.co.uk/art as i took tearure island image

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
find = input("you're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if find =="left":
    print('you\'ve come to a lake. There is an island in the middle of the lake.') # use escape character to use single quote
    choice = input("Now its your choice you wan to swim or wait for boat?"
                   "Type 'swim' or 'wait' \n").lower()
    
    if choice=="wait":
        finaldoor = input("which door you want to open? Red, Blue or Yellow\n").lower()    
        if finaldoor =="red":
            print(" it is a room full of fire so Game over")
        elif finaldoor=="blue":
            print(" you open a door full of water so Game over")
        elif finaldoor=="yellow":
            print(" congrats you find treasure. You Win!!")
        else:
            print("the door that you choose does not exist so Game over")    
    else: # it is called when we swim and when we type anything else then game over message will be printed
        print("Game over")        
else:  # as it is when we move right or tyoe anything then game over message will be printed
    print("Oops you fell into hole so game over!!")



'''
# ![alt text](image.png)
# <!--  the above image is of treasure island project flowchart -->
'''