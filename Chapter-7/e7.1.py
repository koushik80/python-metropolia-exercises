#E-7.1: The random module, coin flipping

#Problem:The first exercise in this chapter consists of simple module library operations.
#In the chapter, a module called random was introduced.
#This module consists of several functions which can be used to get random numbers.
#The idea here is to create a program, which simulates coin flips by randomly selecting 0 (Tails) or 1 (Heads) and printing out the result. 
#When working correctly, the program prints out something like this:

from random import randint
                          #>>>
                          #Heads!
#Obviously, as the program applies random activities,
#it may give any combination of five heads or tails.
#For example, running the program a second time resulted in this:

                         #5 coin flips:
                         #Tails!
                         #Heads!
                         #Heads!
                         #Tails!
                         #Heads!

#Solution:

import random

print("5 coin flips:")
numbers = []
#picks 5 random numbers from 0 to 1
while True:
    if len(numbers) == 5:
        break
    pick = random.randint(0, 1)
    #print(pick)
    numbers.append(pick)


#0 == Tails; 1 == Heads
for i in numbers:
    if i == 0:
        print("Tails!")
        break
    else:
        print("Heads!")


