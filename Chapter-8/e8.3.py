#E-8.3:Calculator: Checking input validity

#Problem:The third exercise in the chapter continues with the calculator exercises done earlier.
#This time the idea is to finally take out the annoying problems with numbers,
#input validity and the stability problems caused by type conversion funvtion.

#Make the following changes to the calculator:
#Every time the user gives numbers to the program,
#the system asks for the numbers with the prompt "Give a number: "
#and continues until a valid number is given.
#If the number is not correct, the system gives an error message "This input is invalid.".
#If the calculator works correctly, it prints out the following:

                    #>>>
                    #Calculator
                    #Give a number: hah, NEVER
                    #This input is invalid.
                    #Give a number: What?
                    #This input is invalid.
                    #Give a number: 100
                    #Give a number: Just kidding
                    #This input is invalid.
                    #Give a number: 50
                    #(1) +
                    #(2) -
                    #(3) *
                    #(4) /
                    #(5)sin(number1/number2)
                    #(6)cos(number1/number2)
                    #(7)Change numbers
                    #(8)Quit
                    #Current numbers: 100 50
                    #Please select something(1-6): 2
                    #The result is: 50
                    #(1) +
                    #(2) -
                    #(3) *
                    #(4) /
                    #(5)sin(number1/number2)
                    #(6)cos(number1/number2)
                    #(7)Change numbers
                    #(8)Quit
                    #Current numbers: 100 50
                    #Please select something(1-6): 8
                    #Thank you!
                    #>>>

#The easiest way of implementing this feature is probably to define a separate function to call when asking numbers.
#In this function, an iteration keeps asking a number as long as the user decides to joke around.
#If the input is valid, iteration terminates with break and the function returns an acceptable value.

#Solution:

import math


print("Calculator")

def putValue():

    while True:
        try:
            number = int(input("Give a number: "))
            break
        except ValueError:
            print("This input is invalid.")
            continue

    return number

number_1 = putValue()
number_2 = putValue()

while True:
    print("""(1) +
(2) -
(3) *
(4) /
(5) sin(number1 / number2)
(6) cos(number1 / number2)
(7) change numbers
(8) Quit""")

    print("Current numbers: ", number_1, number_2)
    selection = int(input("Please select something (1-6): "))

    if selection == 1:
        print("The result is:", number_1 + number_2)
    elif selection == 2:
        print("The result is:", number_1 - number_2)
    elif selection == 3:
        print("The result is:", number_1 * number_2)
    elif selection == 4:
        print("The result is:", number_1 / number_2)
    elif selection == 5:
        print("The result is:", math.sin(number_1 / number_2))
    elif selection == 6:
        print("The result is:", math.cos(number_1 / number_2))
    elif selection == 7:
        number_1 = putValue()
        number_2 = putValue()
    elif selection == 8:
        print("Thank you!")
        break
    else:
        print("Wrong input.")




