
import re # RegEx module

print("This is a calculator.")
print("Type 'quit' when you want to stop.\n")

value = 0
run = True
# variable scope

def performMath():
    global run
    global value
    if value == 0:
        equation = input("Enter the equation: ")
    else:
        equation = input(str(value)) # print the previous value and take an input on the side

    if equation == 'quit':
        print("Goodbye, hooman.")
        run = False
    else:
        equation = re.sub('[^0-9-/*%+.]','',equation)

        if value == 0:
            value = eval(equation) # evaluates when it is the first input or when previous is 0.
        else:
            value = eval(str(value) + equation) # evaluates the previous value and the current value

        print(value)

while run:
    performMath()
