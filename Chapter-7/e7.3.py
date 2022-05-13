#E7.3: Creating own module

#Problem: The third exercise of this chapter goes back from game programming to a more serious line,
#and discusses the creation of self-made modules.
#Unlike other exercises, in this exercise the idea is not to create a full program,
#but only to write a module for existing software.

#In the exercise, we already have the main program in the module, which is as follows:

                        #import mymodule
                        #mymodule.printme("Exampleline")

#The objective is to implement this mymodule-module applied in the exercise.
#Create a module, which has a function printme,
#which prints the given parameter with the disclaimer
#"I got:" and after that, "The parameter was [length] characters long."
#When the module is implemented correctly, the program prints out the following:

                        #I got: Exampleline
                        #The parameter was 11 characters long.

#Solution:
#Note: There's a seperate file mymodule.py in this folder

#mymodule.py

#def printme(result):
    #length = len(result)
    #print("I got: ", "Exampleline")
    #print("The parameter was", length, "characters long.")

import mymodule

def main():
     mymodule.printme("Exampleline")


