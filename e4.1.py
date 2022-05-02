#E-4.1:While-structure
#Problem: Create a program which on each turn prints the round number.
#Start by the round number 0 and make the iteration continue for four loops.
#When the program works correctly, it prints out something like this:

     #This is lap 0
     #This is lap 1
     #This is lap 2
     #This is lap 3
     #This is lap 4

#Solution:

number = 0

while number < 5:
    print("This is lap", number)
    number += 1
