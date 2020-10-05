#  continuous mathematical operation (like a calculator)

import re

print("This is a calculator.")
print("Type 'quit' when you want to stop.\n")

value = 0
run = True
#  variable scope

def performMath():
    global run
    global value
    if value == 0:
        equation = input("Enter the equation: ")
    else:
        # print the previous value and take an input on the side
        equation = input(str(value))

    if equation == 'quit':
        print("Goodbye, hooman.")
        run = False
    else:
        equation = re.sub('[^0-9-/*%+.]','',equation)

        if value == 0:
            # evaluates when it is the first input or when previous is 0.
            value = eval(equation)
        else:
            value = eval(str(value) + equation)

        print(value)

while run:
    performMath()
