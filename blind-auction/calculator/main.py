
from art import image
print(image)
print("welcome to  your own build calculator")

def add(n1,n2):
     return n1+n2
def sub(n1,n2):
     return n1-n2
def mul(n1,n2):
     return n1*n2   
def divide(n1,n2):
     return n1/n2       

    #  add above 4 func in dic


operation =  {
 "+": add,
 "-": sub,
 "*": mul,
 "/": divide,
}

'''
we can also add one by one 
operation = {}  # Create an empty dictionary first

operation["+"] = add
operation["-"] = sub
operation["*"] = mul
operation["/"] = divide
'''

def calculator():
    num1= int(input("enter the first number:"))
    should_hold= True
    while should_hold:
        for  symbol in operation:
            print(symbol)

        opern_syb = input("enter any operation symbol ")
        num2 = int(input("enter the second number:"))
        answer = operation[opern_syb](num1,num2)
        print(f"enter {num1} {opern_syb} {num2} = {answer}")
        cont = input("do you want to continue? yes/no  if yes then we have to perform operation continue with answer : if no then take new different variables for calculation").lower()
        if cont == "yes":
            num1 = answer
        else:
            should_hold= False
            print("\n"*20)
            calculator()     # this is called as recursion


calculator()
