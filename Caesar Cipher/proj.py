import art as art

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(art.logo)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift= int(input("Type the shift number:\n"))

# def encrypt(orginal_text,shift):
#     cipher_text=""
#     for letter in orginal_text:
#         shifted_it = alphabet.index(letter)+shift
#         shifted_it= shifted_it%len(alphabet)
#         cipher_text+=alphabet[shifted_it]
#     print(f"The encoded text is:{cipher_text}")

# encrypt(orginal_text=text,shift=shift)


# def decrypt(text, shift):
#     output_text=""
#     for letter in text:
#          shiftby = (alphabet.index(letter)-shift)%len(alphabet)
#          output_text+=alphabet[shiftby]
#     print(f"The decoded text is:{output_text}")     
# decrypt(text=text,shift=shift)

#  i am commenting encryppt and decrypt function because we can use the same function for both encrypt and decrypt that is caesar cipher

def caesar(text, shift, direction, encode_decode):
    output_text=""
    if encode_decode == "decode":
               shifted = shift*-1
    for letter in text:
        if letter not in alphabet:
            output_text+=letter
        else:    
            
            shiftby = (alphabet.index(letter)+shift)%len(alphabet)
            output_text+=alphabet[shiftby]
    print(f"The {encode_decode}d text is:{output_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift= int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift, direction=direction, encode_decode=direction)
    start_again= input("type yes if you want to go again otherwise type no\n").lower()
    if start_again != "yes":
            should_continue = False
            print("Goodbye")


