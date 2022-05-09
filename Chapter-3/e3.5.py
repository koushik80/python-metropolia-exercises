#E3.5-Calculator, different types of calculations
#Problem:In this exercise, expand the calculator so that the user can select what kind of calculation is done.
#If the user chooses 1, the calculator does addition as earlier.
#If 2, the calculator does substraction,
#if 3, it does multiplication,
#if 4, division.
#Also add the instructions for the user to know what to do as shown in the example below.
#Also, if the user selects anything else besides 1-4, the program prints "Selection was not correct.".
#When working correctly, the progam looks like the following:

#Calculator
#Give the first number: 100
#Give the second number: 25
#(1) +
#(2) -
#(3) *
#(4) /
#Please select something(1-4): 3
#The result is : 2500

#If the user selects something else besides 1-4, it prints the following:

#Calculator
#Give the first number: 320
#Give the second number: 225
#(1) +
#(2) -
#(3) *
#(4) /
#Please select something(1-4): 100
#Selection was not correct.

#Errors such as the user giving input which is not a number, or division by 0, can be ignored at this point.

#Example output:

#Calculator
#Give the first number: 1
#Give the second number: 2
#(1) +
#(2) -
#(3) *
#(4) /
#Please select something(1-4): 200
#Selection was not correct.

#Solution:

print("Calculator")
number_1 = int(input("Give the first number: "))
number_2 = int(input("Give the second number: "))

print("""(1) +
(2) -
(3) *
(4) /""")

select = int(input("Please select something (1-4): "))

if select == 1:
    print("The result is:", number_1 + number_2)
elif select == 2:
    print("The result is:", number_1 - number_2)
elif select == 3:
    print("The result is:", number_1 * number_2)
elif select == 4:
    print("The result is:", number_1 / number_2)
else:
    print("Selection was not correct.")
