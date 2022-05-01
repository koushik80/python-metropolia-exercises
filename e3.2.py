#E3.2
#Problem:
#The idea is to create a program which asks for a user name and password.
#If the given name is wrong, the program prints "The given name is wrong".
#If the name is acceptable, the program asks for the password.
#If the password is correct, the system prints "Both inputs are correct!", otherwise "The password is incorrect.".
#The correct inputs should be "John" and the password "ABC123".
#Overall, the program should print the following:

#Give name: Peter
#The given name is wrong.

#or alternatively

#Give name: John
#Give password: Monkeys?
#The password is incorrect.

#or alternatively

#Give name: John
#Give password: ABC123
#Both inputs are correct!

#Solution:

name = str(input("Give name: "))
if name == "John":
    password = input("Give password: ")
    if password == "ABC123":
         print("Both inputs are correct!")
     else:
         print("The password is incorrect.")
else:
    print("The given name is wrong.")

