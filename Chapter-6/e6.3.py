#E-6.3: Default parameters

#Problem:Create a program which has a main function
#and a subfunction called tester.
#The main function prompts user for an input "Write something (quit ends): "
#and sends this input to the subfunction as a parameter.

#Define the subfunction tester so that it has one parameter called "givenstring",
#which has the default value "Too short".
#If the user input is less than 10 characters,
#the program uses the default value and if 10 or more,
#it prints the usergiven input.
#If the user inputs "quit", the program is terminated.
#When working correctly, the program will print out something like this:
                #>>>
                #Write something(quit ends): what?
                #Too short
                #Write something(quit ends): What do you mean?
                #What do you mean?
                #Write something(quit ends): Ok thats it
                #Ok thats it
                #Write something(quit ends): I am out of here
                #I am out of here
                #Write something(quit ends): quit
                #>>>

#The easiest way of testing the length of a string is by using the function len().

#Solution:

def main():
    while True:
        userInput = input("Write something (quit ends): ")
        if userInput == 10:
            tester()
        elif len(userInput) >= 10:
            tester(userInput)
        elif userInput == "quit":
            break
        else:
            tester()

def tester(givenstring = "Too short"):
    print(givenstring)

if __name__ == "__main__":
    main()
