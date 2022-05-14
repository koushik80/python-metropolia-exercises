#E-7.5: Calculator: math-library

#Problem: This exercise expands on the calculator,
#which was made in chapter 4, exercise 4.
#In this exercise, add sin() and cos()
#-calculations from the library module math to the calculator.
#Add these actions as selections 5 and 6,
#simultaneously moving the "change numbers" feature to 7 and "Quit" to 8.
#When the user calls either of the new features,
#the first number is the divident and second the divider like this: sin(number_1/number2).
#When correctly implemented, the program prints the following:

                                #>>>

                                #Calculator
                                #Give the first number: 1
                                #Give the second number: 2
                                #(1) +
                                #(2) -
                                #(3) *
                                #(4) /
                                #(5)sin(number1/number2)
                                #(6)cos(number1/number2)
                                #(7)Change numbers
                                ##(8)Quit
                                #Current numbers: 1 2
                                #Please select something(1-6): 5
                                #The result is: 0.479425538604203
                                #(1) +
                                #(2) -
                                #(3) *
                                #(4) /
                                #(5)sin(number1/number2)
                                #(6)cos(number1/number2)
                                #(7)Change numbers
                                #(8)Quit
                                #Current numbers: 1 2
                                #Please select something(1-6): 6
                                #The result is: 0.8775825618903728
                                #(1) +
                                #(2) -
                                #(3) *
                                #(4) /
                                #(5)sin(number1/number2)
                                #(6)cos(number1/number2)
                                #(7)Change numbers
                                #(8)Quit
                                #Current numbers: 1 2
                                #Please select something(1-6): 8
                                #Thank you!

                                #>>>


#Solution:

import math

print("Calculator")
number_1 = int(input("Give the first number: "))
number_2 = int(input("Give the second number: "))


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
        number_1 = int(input("Give the first number: "))
        number_2 = int(input("Give the second number: "))
    elif selection == 8:
        print("Thank you!")
        break
    else:
        print("Wrong input.")
