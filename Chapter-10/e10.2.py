#E-10.2: Using the list

#Problem: In the second exercise the idea is to create a small grocery shopping list with the list datastructure. 
#In short, create a program that allows the user to
#(1) add products to the list, (2) remove items and (3) print the list and quit.

#If the user adds something to the list,
#the program asks "What will be added?: "
#and saves it as the last item in the list.
#If the user decides to remove something,
#the program informs the user about how many items there are on the list (There are [number] items in the list.")
#and prompts the user for the removed item ("Which item is deleted?: ").
#If the user selects 0, the first item is removed.
#When the user quits, the final list is printed for the user
#"The following items remain in the list:" followed by the remaining items one per line.
#If the user selects anything outside the options, including when deleting items,
#the program responds "Incorrect selection.".
#When the program works correctly it prints out the following:

                    #>>>
                    #Would you like to
                    #(1)Add or
                    #(2)Remove items or
                    #(3)Quit?: 1
                    #What will be added?: Apples
                    #Would you like to
                    #(1)Add or
                    #(2)Remove items or
                    #(3)Quit?: 1
                    #What will be added?: Beer
                    #Would you like to
                    #(1)Add or
                    #(2)Remove items or
                    #(3)Quit?: 1
                    #What will be added?: Carrots
                    #Would you like to
                    #(1)Add or
                    #(2)Remove items or
                    #(3)Quit?: 2
                    #There are 3 items in the list.
                    #Which item is deleted?: 3
                    #Incorrect selection.
                    #Would you like to
                    #(1)Add or
                    #(2)Remove items or
                    #(3)Quit?: 2
                    #There are 3 items in the list.
                    #Which item is deleted?: 2
                    #Would you like to
                    #(1)Add or
                    #(2)Remove items or
                    #(3)Quit?: 2
                    #There are 2 items in the list.
                    #Which item is deleted?: 0
                    #Would you like to
                    #(1)Add or
                    #(2)Remove items or
                    #(3)Quit?: 4
                    #Incorrect selection.
                    #Would you like to
                    #(1)Add or
                    #(2)Remove items or
                    #(3)Quit?: 3
                    #The following items remain in the list:
                    #Beer
                    #>>>

#Solution:

list = []
while True:

    try:
        customer = int(
            input("Would you like to \n(1)Add or \n(2)Remove items or\n(3)Quit?:"))
    except Exception:
        print("Incorrect selection: Try again")

    if customer == 'end':
        break
    elif customer == 1:
        list.append(input("What will be added?: "))
    elif customer == 2:
        print("There are", len(list), "items in the list.")
        itemToDelete = int(input("Which item is deleted?: "))
        try:
            list.pop(itemToDelete)
        except Exception:
            print("Incorrect selection.")
    elif customer == 3:
        print("The following items remain in the list:")
        for i in list:
            print(i)
        break
    else:
        print("Incorrect selection.")
