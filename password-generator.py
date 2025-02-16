
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")

tot_letters = int(input("How many letters would you like in your password?\n"))
tot_numbers = int(input("How many numbers would you like in your password?\n"))
tot_symbols = int(input("How many symbols would you like in your password?\n"))

# easy password

# password = ""
# for char in range(0,tot_letters):
#     password+=random.choice(letters)

# for char in range(0,tot_numbers):
#     password+=random.choice(numbers)

# for char in range(0,tot_symbols):
#     password+=random.choice(symbols)

# print(password)    

# hard password

password_list = []
for char in range(0,tot_letters):
    password_list.append(random.choice(letters))

for char in range(0,tot_numbers):
    password_list.append(random.choice(numbers))

for char in range(0,tot_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
#  it is like ["a","1","%","&","3","b","c"] now to convert it into string we have to one variable na add that in it
password = ""
for char in password_list:
    password+=char
print(f"your password is : {password}")
   