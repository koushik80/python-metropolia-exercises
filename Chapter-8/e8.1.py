#E-8.1: Basic exception handler

#Problem: The first exercise in this chapter discusses the most common problem with programs in Python:
#getting a numeric value as input without a problem or constant fear of TypeError.
#Simply put, create a program, which asks the user for input and tries to convert it to an integer value.
#If the conversion happens without problems, the program prints "The input was suitable!".
#If the user gives something which does not convert, like letters or special characters,
#the program avoids the error with an exception handler and prints "The input was malformed.".
#When working correctly, the program prints out the following:


                    #Give a number: Monkeys?
                    #The input was malformed.

#or alternatively

                    #Give a number: 234
                    #The input was suitable!

#Probably the best way of implementing this exercise is to use the generic error class Exception,
#as there are some special cases where the interpreter actually raises something else than TypeError,
#like ValueError or NameError.
#Also keep in mind, that there can be an else-segement in the exception handler.


#Solution:

myNumber = input("Give a number: ")

try:
    myNumber = int(myNumber)

except Exception:
    print("The input was malformed.")

else:
    print("The input was suitable!")

