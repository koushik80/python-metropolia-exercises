#E3.3
#Problem:The third exercise is to create a conditional structure which prints a line depending on the given selection.
#The program asks a number between 1 and 3,
#and based on the number prints the following:
#1 prints "You selected one.",
#2 prints "You selected two."
#and 3 prints "You selected three.", like this:

    #Select a number (1-3): 2
    #You selected two.

#Solution:

select_1 = "You selected one."
select_2 = "You selected two."
select_3 = "You selected three."

target = int(input("Select a number(1-3): "))

if 0 < target < 4:
    if target == 1:
        print(select_1)
    elif target == 2:
        print(select_2)
    else:
        print(select_3)
else:
    print("Invalid input")


