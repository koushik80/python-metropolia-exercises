#E3.4-Using several parameters
#Problem:In the fourth exercise the idea is to define an if-structure which decides the action based on several inputs.
#The program asks for two numbers. If both of the numbers are even, the program prints "Both numbers are even."
#If only one of the numbers is even, the program prints "One of the numbers is even.".
#Finally, if neither of the numbers is even, the program prints "Both numbers are odd".
#When correct, the program works as following:

#Give a number: 10
#Give another number: 11
#One of the numbers is even.

#or alternatively

#Give a number: 12
#Give another number: 20
#Both numbers are even.

#or alternatively
#Give a number: 15
#Give another number: 21
#Both numbers are odd.

#Solution:


number_1 = int(input("Give a number: "))
number_2 = int(input("Give another number: "))

if number_1 % 2 == 0 and number_2 % 2 == 0:
    print("Both numbers are even.")
elif number_1 % 2 == 0 or number_2 % 2 == 0:
    print("One of the numbers is even.")
else:
    print("Both numbers are odd.")
