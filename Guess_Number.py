

logo = '''

#   / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
#  / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
# / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
# \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|     
#  '''

print(logo)
'''
print("Welcome to the Number Guessing Game!")
print("I am thinking of numbers b/w 1 to 100")
print("answer ro win this game is 68")
choose = input("Type 'easy' or 'hard' " ).lower()

def foreasy():
        print("you have total 10 attemps remaining  to guess a number")
        total= 10
        total_attempt =True
        while total_attempt:
            choice= int(input("Make a guess : "))
            total -= 1
            if choice == 68:
                print("you have guessed the number correctly")
                total_attempt = False
            elif choice < 68:
                print("too low")
                print(f"you have remaining {total} attempts")
                
            else:
                print("too high")
                print(f"you have remaining {total} attempts")
            if total == 0:
                print("you have run out of guesses, you lose")
                total_attempt = False

def forhard():
        print("you have total 5 attemps remaining  to guess a number")
        total= 5
        total_attempt =True
        while total_attempt:
                choice= int(input("Make a guess : "))
                total -= 1
                if choice == 68:
                    print("you have guessed the number correctly")
                    total_attempt = False
                elif choice < 68:
                    print("too low")
                    print(f"you have remaining {total} attempts")
                    
                else:
                    print("too high")
                    print(f"you have remaining {total} attempts")
                if total == 0:
                    print("you have run out of guesses, you lose")
                    total_attempt = False                

if choose == 'easy':
    foreasy()
else:
     forhard()
#  the above is too long way to do that i think the short way to do this is :
'''

import random;
print("Welcome to the Number Guessing Game!")
print("I am thinking of numbers b/w 1 to 100")

answer = random.randint(1,100)
print(f"the answer which i guess is {answer}")
choice = input("Type 'easy' or 'hard' " ).lower()

def total(attempts,answer):
    while attempts>0:
        choose = int(input("Guess the number: "))
        attempts -= 1
        if choose == answer:
            print("you have guessed the number correctly")
            return
        elif choose < answer:
                print("too low")
                print(f"you have remaining {attempts} attempts")
                        
        else:
            print("too high")
            print(f"you have remaining {attempts} attempts")
        if attempts == 0:
            print("you have run out of guesses, you lose")
             



if choice == 'easy':
    attempts = 10
else:
    attempts = 5

total(attempts,answer)    

