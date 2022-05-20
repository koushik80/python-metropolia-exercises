#E-9.3: Initializing a class

#Problem: In the third exercise we make one final adjustment to the class by adding initialization data and a docstring.
#First add a docstring "Player-class: stores data on team colors and points.".
#After this, add an initializing method __init__ to the class,
#and make it prompt the user for a new player color with the message"What color do I get?: ".

#Edit the main function to first create two player objects from the class,
#player1 and player2. After this, make the program call player1's method "goal" twice and player2's goal once. 
#After this, call both objects with the method "tellscore".
#If everything went correctly, the program should print something like this:

                #>>>

                #What color do I get?: Blue
                #What color do I get?: Red
                #I am Blue, we have 2 points!
                #I am Red, we have 1 points!

                #>>>

#Solution:

class Player:
    teamcolor = "Blue"
    points = 0

    def __init__(self):
        self.teamcolor = input("What color do I get?: ")

    def tellscore(self):
        print("I am " + self.teamcolor + ", we have" +
              str(self.points) + " points!")

    def goal(self):
        self.points += 1

    def printout(self):
        print("The" + self.teamcolor + " contender has " +
              str(self.points) + " points!")


def main():
    team_player_1 = Player()
    team_player_2 = Player()
    team_player_1.goal()
    team_player_1.goal()
    team_player_2.goal()
    team_player_1.tellscore()
    team_player_2.tellscore()


if __name__ == "__main__":
    main()
