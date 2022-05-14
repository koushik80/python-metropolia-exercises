#E-7.6: Notebook: Adding dates to the system

#Problem:The last exercise in this chapter adds
#a small feature to the other continuous exercise project, the notebook.
#In this exercise, add a feature which includes the date and time of the written note to the program.
#The program works as earlier,
#but saves data in the form "[note]:::[date and time]"
#meaning that there is a three-colon separator between the note and timestamp.
#The timestamp can be generated as follows:

                    #>>> import time

                    #>>> time.strftime("%X %x")
                    #'19:01:34 01/03/09'
                    #>>>

#This returns the date and time in a nice, compact string.
#When working correctly, the program prints the following:

                    #>>>

                    #(1) Read the notebook
                    #(2) Add note
                    #(3) Empty the notebook
                    #(4) Quit

                    #Please select one: 2

                    #Write a new note: Call mom.
                    #(1) Read the notebook
                    #(2) Add note
                    #(3) Empty the notebook
                    #(4) Quit

                    #Please select one: 1
                    #Call mom.:::11:44:41 04/25/11

                    #(1) Read the notebook
                    #(2) Add note
                    #(3) Empty the notebook
                    #(4) Quit

                    #Please select one: 4
                    #Notebook shutting down, thank you.
                    #>>>

#Solution:

#Note: There's a seperate file notebook.txt in this folder

import time


while True:
    print("""
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit""")

    select = int(input("Please select one: "))

    if select == 1:
        notebook = open("notebook.txt", "r")
        print(notebook.read())
        notebook.close()
    elif select == 2:
        notebook = open("notebook.txt", "a")
        text = str(input("Write a new note:  "))
        time = time.strftime("%X %x")
        notebook.write(text + ":::" + time)
        notebook.close()
    elif select == 3:
        notebook = open("notebook.txt", "w")
        print("Notes deleted.")
        notebook.close()
    elif select == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection")
