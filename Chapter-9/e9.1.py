#E9.1: Creating a class and an object

#Problem:Create a program which has a class Player,
#which has two attributes, teamcolor and points.
#Then create a main function which creates an object from this class,
#gives its attributes values "Blue" and "300".
#After this,make the program print
#the object data in the form "The [color] contender has [points] points!" like this:

                    #>>>
                    #The Blue contender has 300 points!
                    #>>>

#Solution:

class Player:
    teamcolor = "Blue"
    points = "300"

    def printout(self):
        print("The " + self.teamcolor + " contender has " + self.points + " points!") 

def main():
    team_player = Player()
    team_player.teamcolor = "Blue"
    team_player.points = "300"
    team_player.printout()

if __name__ == '__main__':
    main()
