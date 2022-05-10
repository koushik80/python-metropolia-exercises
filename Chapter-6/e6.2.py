#E-6.2: Using parameters

#Problem:Create a program which has the main function and a subfunction "poweroftwo".
#The main function prompts the user for a number "Give a number: "
#and then this number is sent to the subfunction as a parameter.
#The subfunction calculates the n:th power of 2 of the number
#(if given 3, 2*2*2; if 5, 2*2*2*2*2 and so on, 2**[number])
#and prints it out with the message "The result was [result]".
#When working correctly, the program prints:

                 #Give a number: 9
                 #The result is 512
#Also remember to add this main function call to the main level:

                 #if __name__ == "__main__":
                      #main()

#Solution:

def main():
    numValue = (int(input("Give a number: ")))
    poweroftwo(numValue)

def poweroftwo(num):
    num = 2 ** num
    print("The result is", num)

if __name__ == "__main__":
    main()

