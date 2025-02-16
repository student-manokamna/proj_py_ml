
from art import logo,vs
from data import data

def format(account):
    name = account['name']
    description = account['description']
    followers = account['follower_count']
    return f"Account: {name}, Description: {description}, Follower: {followers}"


def check(guess,Account_A_follwer, Account_B_follwer):
    if Account_A_follwer>Account_B_follwer:
         return guess=='a'
    else:
        return guess=='b'

total_score=0           
print(logo)

#  as first  now we want toc choose a random people account from data.py


import random
Account_B= random.choice(data)
continue_it = True
while continue_it:
    Account_A = Account_B
    # Account_A = random.choice(data)
    Account_B = random.choice(data)
    #  if both come some then again take account_b
    if Account_B == Account_A:
        Account_B = random.choice(data)

    #  format the aqccount data
    print(f"Compare_A: {format(Account_A)}")  
    print(vs)
    print(f"Against_B: {format(Account_B)}")      
    # user guess a input 
    guess = input("Who has more follower type 'A' or 'B': ").lower()
    #  we want to clear the screen

  


    # now check who has more follower

    Account_A_follwer = Account_A["follower_count"]
    Account_B_follwer = Account_B["follower_count"]
    #  so create a func to check it

    it_correct = check(guess, Account_A_follwer,Account_B_follwer) 
    #  if it is correct then print you win else you lose
    print("\n"*20)
    print(logo)
    if it_correct:
        total_score+=1
        print(f"You're right! Current score: {total_score}")
    else:
        print(f"Sorry, that's wrong. Final score: {total_score}")
        continue_it = False



          
