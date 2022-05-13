#E-7.2: Nuke-foot-cockroach

#Problem: The second exercise in this chapter continues with random selection.
#In this exercise the objective is to develop a game called nuke-foot-cockroach,
#which is pretty similar to the more popular variant,paper-rock-scissors.
#The rules are simple: both players select either nuke,
#foot or cockroach, and the winner is determined in the following way:
#Foot beats cockroach, nuke beats foot and cockroach beats nuke.
#If both the player and the AI select the same, it's a tie, except if both choose nuke, then both lose.

#Implement the game so that the other player is computer controlled,
#and chooses randomly either foot(number 1),
#cockroach(number 3) or nuke(number 2).
#Also implement a feature which keeps the score, calculating both rounds the player won, and ties.
#If the player wins, print "You WIN!", if they loose "You LOSE!".
#If the round was a tie, either "It is a tie!" or "Both LOSE!", depending on if the tie was caused by a nuke or not.
#If the player selects "quit", the game ends and the final score is given. When the game works correctly, it prints the following:


                    #Foot, Nuke or Cockroach? (Quit ends): Foot
                    #You chose: Foot
                    #Computer chose: Nuke
                    #You LOSE!
                    #Foot, Nuke or Cockroach? (Quit ends): Spaceshuttle
                    #Incorrect selection.
                    #Foot, Nuke or Cockroach? (Quit ends): Cockroach
                    #You chose: Cockroach
                    #Computer chose: Nuke
                    #You WIN!
                    #Foot, Nuke or Cockroach? (Quit ends): Cockroach
                    #You chose: Cockroach
                    #Computer chose: Nuke
                    #You WIN!
                    #Foot, Nuke or Cockroach? (Quit ends): Quit
                    #You played 3 rounds, and won 2 rounds, playing tie in 0 rounds.

#Solution:

from random import randint


def sub(computer):
    if computer == 1:
        computer = "Foot"
    elif computer == 2:
        computer = "Nuke"
    elif computer == 3:
        computer = "Cockroach"
    print("Computer chose: ", computer)


def main():
    wins = 0
    rounds = 0
    draws = 0

    while True:
        computer = randint(1, 3)
        player = input("Foot, Nuke or Cockroach? (Quit ends): ")

        if player == "Quit":
            print("You played", rounds, "rounds, and won", wins,
                  "rounds, playing tie in", draws, "rounds.")
            break
        elif player == ("Spaceshuttle"):
            print("Incorrect selection.")
        else:
            print("You chose: ", player)
            sub(computer)
            rounds += 1

            if (player, computer) == ("Foot", 1):
                draws += 1
                print("It is a tie!")
            elif (player, computer) == ("Foot", 2):
                print("You LOSE!")
            elif (player, computer) == ("Foot", 3):
                wins += 1
                print("You WIN!")
            elif (player, computer) == ("Nuke", 2):
                print("both loose")
            elif (player, computer) == ("Nuke", 1):
                wins += 1
                print("You WIN!")
            elif (player, computer) == ("Nuke", 3):
                print("You LOSE!")
            elif (player, computer) == ("Cockroach", 1):
                print("You LOSE!")
            elif (player, computer) == ("Cockroach", 2):
                wins += 1
                print("You WIN!")
            elif (player, computer) == ("Cockroach", 3):
                draws += 1
                print("It is a tie!")


if __name__ == "__main__":
    wins = 0
    rounds = 0
    draws = 0
    main()
