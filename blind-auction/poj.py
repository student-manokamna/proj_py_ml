from art import logo ;

print(logo)
print("welcome to secret auction program")
# name = input("Enter your Name.")
# bid = float(input("Enter your bid: $"))

def maximum_bidder(bidder_dic):   # this bidder_dic is the dic1 we created above
    # max_bidder = max(bidder, key=bidder.get) m-1  below m-2

    winner =""
    max_bid = 0
    for bid in bidder_dic:
        if bidder_dic[bid] > max_bid:
            max_bid = bidder_dic[bid]
            winner = bid
    print(f"winner is {winner} with max_bis is {max_bid}")




dic1 ={}
#  save data 
# dic1[name] = bid

# should_continue= input("Ask if there are other user who want to bid. type: 'y' for yes and 'n' for no: ")
#  as above is right but we have to continue it until we have true so put allo above in aloop

continue_until=True
while continue_until:
    name = input("Enter your Name.")
    bid = float(input("Enter your bid: $"))
    dic1[name] = bid
    should_continue= input("Ask if there are other user who want to bid. type: 'y' for yes and 'n' for no: ").lower()
    if should_continue=='n':
        continue_until=False
        maximum_bidder(dic1)
    elif should_continue=='y':
        print("\n"*20)
    else:
        print("you type wrong ")        



          

    



#  todo in it :
# 1. ask user for input
# 2. store user input in a dictionary {name:pirce} so we store as dic1[name]=price
# 3. ask user if there are other user who want to bid
# 4. compare bids in dic


    

