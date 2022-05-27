#E-10.4: Notebook: Using list with the notebook, pickle

#Problem: In this exercise the idea is to build a notebook which applies the Python data structure list as a note manipulation method when the program is executed,
#and saves the data in a bitwise mode with pickle.
#The program has the following features:
#A) It is possible to add notes, with similar timestamps as earlier.
#B)It is possible to edit a note by selecting it from the list, and rewriting it with new data.
#C) It is possible to delete notes separately based on the selection and
#D) Notebook loads an existing notebook file from the file "notebook.dat" if such a file exists.

#When the program starts, the system should check for a notebook datafile "notebook.dat"
#and load it with pickle. If no such file exists,
#or there was a problem with the file, a new file is created and the user is notified "No default notebook was found, created one.".
#After this the basic main menu works as in the earlier notebook:

        #>>>
        #No default notebook was found, created one.
        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 2
        #Write a new note: Buy birdseed.
        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 1
        #Buy birdseed.: : : 16: 41: 40 04/25/11

#If the user is not pleased with a note,
#it is possible to change one note with the option 3.
#Then the program asks for the edited note (0 is the first one on the list) with the prompt "The list has [number] notes.\nWhich of them will be changed?:".
#After giving an input, the user is then printed the selected note and asked for a new note "Give the new note:".
#This new note replaces the old note on the list:

        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 3
        #The list has 1 notes.
        #Which of them will be changed?: 0
        #Buy birdseed.: : : 16: 41: 40 04/25/11
        #Give the new note: Buy pig food.
        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 1
        #Buy pig food.: : : 16: 42: 03 04/25/11

#Deleting a note is done similarly as editing.
#The only real difference is that the deleted note is printed to the user with the notification "Deleted note [deleted note]".

        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 4
        #The list has 1 notes.
        #Which of them will be deleted?: 0
        #Deleted note Buy pig food.:::16:42:03 04/25/11

#Finally, when the user decides to quit, the current notebook is saved as a datagram to the file "notebook.dat",
#with the notification "Notebook shutting down, thank you.".

        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 5
        #Notebook shutting down, thank you.

#Also, if there already is a notebook datagram file,
#it should be loaded at startup, and otherwise normally used in the notebook program:

        #>>>

        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 1
        #Buy gas:::16:45:51 04/25/11
        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 4
        #The list has 1 notes.
        #Which of them will be deleted?: 0
        #Deleted note Buy gas:::16:45:51 04/25/11
        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 2
        #Write a new note: Call tow truck
        #(1) Read the notebook
        #(2) Add note
        #(3) Edit a note
        #(4) Delete a note
        #(5) Save and quit

        #Please select one: 5
        #Notebook shutting down, thank you.
        #>>>

#Solution:

import pickle
import time


file_name = "notebook.dat"

def readfile(file_name):
    while True:
        try:
            handle = open(file_name, 'rb')
            notebook_script = pickle.load(handle)
            handle.close()
            return notebook_script
        except IOError:
            newfile(file_name)
            print("No default notebook was found, created one.")


def writefile(notebook, file_name):
    try:
        writefile = open(file_name, 'wb')
        pickle.dump(notebook, writefile)
        writefile.close()
    except IOError:
        return False


def newfile(file_name):
    try:
        newfile = open(file_name, 'wb')
        notebook = []
        pickle.dump(notebook, newfile)
        newfile.close()
    except IOError:
        return False


def editnote(notebook):
    print("The list has", len(notebook), "notes.")
    try:
        edit_notebook = int(input("Which of them will be changed?:"))
        print(notebook[edit_notebook])
        new_note = input("Give the new note: ")
        new_note = new_note+":::"
        new_note = time.strftime("%X %x")
        notebook[edit_notebook] = new_note
        return notebook
    except Exception:
        print("Incorrect value.")


def deletenote(notebook):
    print("The list has", len(notebook), "notes.")
    try:
        del_note = int(input("Which of them will be deleted?: "))
        del_note -= 1
        print("Deleted note", notebook[del_note])
        notebook.pop(del_note)

        return notebook
    except Exception:
        print("Incorrect value.")


def main():
    notebook = []
    notebook = readfile(file_name)
    while True:
        select = input('''(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit
Please select one: ''')
        if select == '1':
            for i in notebook:
                print(i)
        elif select == '2':
            new_note = input("Write a new note: ")
            new_note = new_note+":::"
            new_note = time.strftime("%X %x")
            notebook.append(new_note)
        elif select == '3':
            notebook = editnote(notebook)
        elif select == '4':
            notebook = deletenote(notebook)
        elif select == '5':
            writefile(notebook, file_name)
            print("Notebook shutting down, thank you.")
            break




if __name__ == "__main__":
    main()
