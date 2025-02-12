
print("welcome to python pizza Deliveries!!")
size = input("what size pizza do you want?  S, M, L:")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
extra_cheese = input("Do you want extra cheese? Y or N:")

bill= 0
if size=='S':
    bill+=15
elif size=='M':
    bill+=20
elif size == 'L':
    bill+=25
else:
    print("you typed unspecified size of pizza!!")

if pepperoni =='Y':
    if size=='S':
        bill+=2
    else: # then add 3 dolar to both medium and large pizza
        bill+=3
        # now for extra cheese add amount in bill and it is same for all size pizza

if extra_cheese=='Y':
    bill+=1

print(f"the final amount is ${bill}.")     
