#E-8.2: Catching several errors at once

#Problem:The second exercise combines several normal error scenarios into one program.
#In this exercise, create a program which prompts the user for a file name.
#Based on user input, open the given file and read the contents into one big string.
#Then convert this string to an integer and divides the number 1000 with the number.
#Finally, print out the result from the division.

#The idea here is that no matter what the user input is, the program works.
#If the file cannot be found, the program prints "There seems to be no file with that name.",
#if the conversion fails, "The file contents are unsuitable.",
#in other errors "There was a problem with the program."
#or if everything went correctly,
#"The result was [result].".
# In any case (besides KeyboardInterruption with Ctrl-C),
#the program should be impossible to break with user input.
#If everything works as intended, it prints the following:

                        #>>>
                        #Give the file name: hahaha...NO
                        #There seems to be no file with that name.
                        #>>>
                        #Give the file name: notebook.txt
                        #The file contents were unsuitable.
                        #>>>

                        #Give the file name: number.txt
                        #The result was 3.194888178913738
                        #>>>

#Solution:

def getfilename():
    filename = input("Give the file name: ")
    return filename


def main():
      execute = getfilename()

      try:
          handle = open(execute, "r")
          filetext = handle.read()
          result = 1000/float(filetext)

      except IOError:
          print("There seems to be no file with that name.")

      except (TypeError, ValueError):
          print("The file contents were unsuitable.")

      else:
          print("The result was", result)


if __name__ == "__main__":
    main()
