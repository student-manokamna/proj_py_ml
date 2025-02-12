    


import hangman_words as words
import hangman_art as art




lives = len(art.stages)-1
print(art.welcome)
print(art.logo)
import random
word_list = ["aardvark", "baboon", "camel"]
choose_word= random.choice(words.word_list)
print(choose_word)

placeholder = ""

for blank in range(len(choose_word)):
     placeholder+="_ "
print(placeholder)
print("\n")
game_over= False
correct_guess = []
while not game_over:
    print(f"**********//{lives}/{len(art.stages)-1}lives left*******")
    user_guess = input("Guess a Letter:").lower()
    if user_guess in correct_guess:
        print(f"you have already guessed {user_guess}")
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
        print(f"{user_guess} is not in the word. You lose a life")
        lives-=1
        if lives==0:   # why this is inside above if bcz if it is outsude then it does not check tje condition that if userguesss is not in choosen word as for if userguess is in choose statement it print for that also so we put it inside that if main if foloow the it move inside 
          game_over=True  # bcz if lives are 0 then game over and break the while loop
          print(f"************** {choose_word}!!you lose*************")    
    if "_" not in strings:
        game_over=True
        print("!!!!!!!!!!!!!!you win !!!!!!!!!!!!!!!!!!")

    #  now we want to print stages acc to guess so we use lives as index to print stages and it is inside while loop so it will print stages acc to guess.at every guess number it should print it
    if lives>=0:
      print(art.stages[lives])
      