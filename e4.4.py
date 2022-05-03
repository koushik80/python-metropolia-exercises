#E4.4-Several options, changing the number
#Problem: The last exercise in this chapter continues with the exercise from the last chapter,
# the calculator. In this exercise, expand the existing code by implementing the following new features:
#(A) Calculator does not automatically quit when the result is given, allowing user to do new calculations. The user has to select "6" in the menu to exit the program.
#(B) The calculator shows the selected numbers in the main menu by printing "Current numbers:" and the user-given input.
#By selecting "5" in the calculator menu, the user can change the given numbers. When implemented correctly, the program prints out following:

                #Calculator
                #Give the first number: 100
                #Give the second number: 25
                #(1) +
                #(2) -
                #(3) *
                #(4) /
                #(5) Change numbers
                #(6) Quit
                #Current numbers: 100 25
                #Please select something(1-6): 5
                #Give the first number: 10
                #Give the second number: 30

                #(1) +
                #(2) -
                #(3) *
                #(4) /
                #(5) Change numbers
                #(6) Quit
                #Current numbers: 10 30
                #Please select something(1-6): 1
                #The result is: 40

                #(1) +
                #(2) -
                #(3) *
                #(4) /
                #(5) Change numbers
                #(6) Quit
                #Current numbers: 10 30
                #Please select something(1-6): 6
                #Thank you!
                #>>>

#Solution:

print("Calculator")
num_1 = int(input("Give the first number: "))
num_2 = int(input("Give the second number: "))


while True:
    print("""(1) +
(2) -
(3) *
(4) /
(5) Change numbers
(6) Quit""")

    print("Current numbers: ", num_1, num_2)
    selection = int(input("Please select something (1-6): "))

    if selection == 1:
        print("The result is:", num_1 + num_2)
    elif selection == 2:
        print("The result is:", num_1 - num_2)
    elif selection == 3:
        print("The result is:", num_1 * num_2)
    elif selection == 4:
        print("The result is:", num_1 / num_2)
    elif selection == 5:
        num_1 = int(input("Give the first number: "))
        num_2 = int(input("Give the second number: "))
    elif selection == 6:
        print("Thank you!")
        break
    else:
        print("Wrong input.")
