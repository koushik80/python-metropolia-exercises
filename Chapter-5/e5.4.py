#E-5.4: Notebook: Read and write to the notebook
#Problem:The last exercise in this chapter is the first part of the second multi-part assignment of this course, the notebook.
#In this notebook the user is able to add, read and delete notes from a separate note file "notebook.txt".
#Create a program which allows the user to
#(1) Read the contents of the notebook
#(2) Add notes to the file or
#(3) Delete all of the notes.
#If the user selects 1,
#the entire notebook file is printed to the screen,
#if 2 then the program prompts "Write a new note: ",
#and adds the written note as the last line into the file with a trailing line break "\n".
#If the player selects 3, the file is emptied and the message "Notes deleted" will be shown.
#Also add the option(4) Quit, which ends the program, printing "Notebook shutting down, thank you.".
#With other selections the program prompts "Incorrect selection". When working, the program prints following:


                #(1) Read the notebook
                #(2) Add note
                #(3) Empty the notebook
                #(4) Quit

            #Please select one: 1
            #Buy milk

               #(1) Read the notebook
               #(2) Add note
               #(3) Empty the notebook
               #(4) Quit

            #Please select one: 2
            #Write a new note: Buy car

               #(1) Read the notebook
               #(2) Add note
               #(3) Empty the notebook
               #(4) Quit

            #Please select one: 1
            #Buy milk
            #Buy car

               #(1) Read the notebook
               #(2) Add note
               #(3) Empty the notebook
               #(4) Quit

            #Please select one: 4
            #Notebook shutting down, thank you.

#Solution:

#Note: There's a seperate file notebook.txt in this folder

while True:
    print("""
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit""")

    select = int(input("Please select one: "))

    if select == 1:
        notebook = open("notebook.txt", "r")
        print(notebook.read()[:-1])
        notebook.close()
    elif select == 2:
        notebook = open("notebook.txt", "a")
        text = str(input("Write a new note:  "))
        notebook.write("{0}\n".format(text))
        notebook.close()
    elif select == 3:
        notebook = open("notebook.txt", "w")
        print("Notes deleted.")
    elif select == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection")
