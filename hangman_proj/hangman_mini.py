
# import random
# word_list = ["aardvark", "baboon", "camel"]
# choose_word= random.choice(word_list)
# print(choose_word)
# placeholder = ""
# for blank in range(len(choose_word)):
#      placeholder+="_ "
# print(placeholder)
# print("\n")
# user_guess = input("Guess a Letter:").lower()
# strings =""
# for char in choose_word:
#     if char==user_guess:
#         strings+=char
#     else:
#         strings+="_"    
# print(strings)        
# for letter in choose_word:  # this is for practice base on the task so you  know what to do in task at starting
#     if letter ==user_guess:
#         print("Right")  
#     else:
#         print("Wrong")    


# using while loop instead of for loop to keep the game running until the user has guessed all the letters in the word.

stages=[r'''
    ____________
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / \
        |
        _|___
            
            ''',
    r'''
    ____________
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / 
        |
        _|___
    ''' ,
    r'''
    ____________
        |/      |
        |      (_)
        |      \|/
        |       
        |      
        |
        _|___
    ''',
    r'''
    ____________
        |/      |
        |      (_)
        |      \|
        |       
        |      
        |
        _|___
    ''',
    r'''
    ____________
        |/      |
        |      (_)
        |       |
        |       
        |      
        |
        _|___
    ''',
    r'''
    ____________
        |/      |
        |       _
        |      
        |       
        |      
        |
        _|___
    '''
       ]
# this r means treat the string as raw string so that we can use \n as it is and it will not be treated as escape sequence. so it will print as it is.

lives = len(stages)-1
import random
word_list = ["aardvark", "baboon", "camel"]
choose_word= random.choice(word_list)
print(choose_word)

placeholder = ""

for blank in range(len(choose_word)):
     placeholder+="_ "
print(placeholder)
print("\n")
game_over= False
correct_guess = [] # see this concwpt in copy
while not game_over:
    user_guess = input("Guess a Letter:").lower()
    strings =""
   
    for char in choose_word:
        if char==user_guess:
            
            strings+=char
            correct_guess.append(char)
        elif char in correct_guess: # we do so that if we guess the correct letter then it should not be replaced by _. so we use this condition. 
            #  as eg: first i guess c which is euql to char in camel so it goes to correctguess then in next turn as game not ovee so 
            # while loop continue then i guess a which is in char so now append a in correctguess but to add it in strings we use elif condition.so that ki jo pichle vala c hh vo bhi dekhe and add it to strings.

            strings+=char    
        else:
            strings+="_"    
    print(strings) 
    if user_guess not in choose_word:
        lives-=1
        if lives==0:   # why this is inside above if bcz if it is outsude then it does not check tje condition that if userguesss is not in choosen word as for if userguess is in choose statement it print for that also so we put it inside that if main if foloow the it move inside 
          game_over=True  # bcz if lives are 0 then game over and break the while loop
          print("**************you lose*************")    
    if "_" not in strings:
        game_over=True
        print("!!!!!!!!!!!!!!you win !!!!!!!!!!!!!!!!!!")

    #  now we want to print stages acc to guess so we use lives as index to print stages and it is inside while loop so it will print stages acc to guess.at every guess number it should print it
    if lives>=0:
      print(stages[lives])
      



        # what r its todo as per the task
# 1. Create a word list to choose a random word from.
# 2. Create a blank spaces for the word. blank space size is equal to the length of the word is you guess the word.
# 3. Ask the user to guess a letter.
# 4. Check if the letter is in the word, if it is add it to the blank spaces.by making a new string with the guessed letter in the correct position. If it is not in the word, add a blank space to the string. 
# 5. If the letter is not in the word, print a message saying it is wrong
# 6. now use of while loop instead of for loop to keep the game running until the user has guessed all the letters in the word.
# 7. as problem in for loop is that it will only run once and then stop.and the letter which we get is removed when we again guess the letter. so to store previous letter we use while loop.
# 8. if all _ are replaced by the letter then game is over.means its true now further while loop will not run.
# 9. see hume game-over vali condition kaise pta chli as hum tab tk letter guess krte jayege jab tk spaces m letter na aa jaye jaise hi wo aa jaye to game over ho jayega.
# 10. so we use if statement to check if the string is equal to the word then game over.
# 11. now we use game_over=True to stop the while loop.
# 12. change this for loop is it is not updating value so for that we use list in which we store values
# 13. if guess is not in choosen word then lives will be decreased by 1.
# 14. if lives are 0 then game over.
# new file hangman.py

#  i want to take word list live we can say from module so we import that module (see hard coded data before)
#  todo as per the task
# 1. update the word list to use the 'word' module from the python standard library. from hangman_words.py
# from hangman_proj import hangman_words if it is folder we take it like this 
# 2. is update the code below to use the 'word_list' from the 'word' module. which is hangman_words.py module in the hangman_proj folder. 
#  so for that get stages from hangman_art.py and word_list from hangman_words.py and then use it in the code.so i delted previous stages 
# this r means treat the string as raw string so that we can use \n as it is and it will not be treated as escape sequence. so it will print as it is.
#  todo 3. is import logo from hangman_art.py and print it at the start of the game.
# todo.4 is if user guess the corretc letter that already guess then it should be printed and tell to user that u have already guessed that letter.
# todo.5 if letter u guess is not in choosen word tell that u have guessed wrong letter.by print it 
#  so handle it where y write if userguess is not in chhosen woord
# todo6. tell user that how many lives are left.
#  so it is  after while not gameover 
# tood.7 tell user that he lose bcz he type wrong letter by mention it 