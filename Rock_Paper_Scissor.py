
rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''' 
game_images = [rock,paper,scissor]

import random
user_choice = int(input("what you choose: 0 for rock, 1 for paper, 2 for scissor\n"))
if user_choice>=0 and user_choice<=2:
   print(game_images[user_choice])  # as here we are taking user input so we are printing user choice and its index will give us that particular image 

computer_choice= random.randint(0,2)
# print(f"computer choose {computer_choice}") instead of this i want an image so we get that by
print("Computer choose: ")
print(game_images[computer_choice])
if user_choice>=3 or user_choice<0:
     print("you choose invalid number so you lose")  
elif user_choice==0 and computer_choice==2:
    print("computer choose scissor so you win")
elif user_choice==2 and computer_choice==0:
    print("computer choose rock so you lose")
elif user_choice>computer_choice:
    print("you win")
elif user_choice<computer_choice:
    print("you lose")
elif user_choice==computer_choice:
    print("It's a draw")

                 
