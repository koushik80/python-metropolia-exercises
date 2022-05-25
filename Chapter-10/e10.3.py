#E-10.3: More list methods

#Problems: The third exercise also revolves around list methods,
#this time doing data manipulation.
#In the same folder as the source code,
#there is a file named "words.txt", which has a randomly selected set of words.
#Build a program, which reads all of the words from the file,
#sorts them in alphabetic order and prints out the list with the statement "Words in an alphabetical order:".
#When correctly implemented, the program prints out the following:

                        #>>>
                        #Words in an alphabetical order:
                        #aardvark
                        #beercase
                        #buzz
                        #hammer
                        #house
                        #lion
                        #nail
                        #roadworks
                        #salesman
                        #shovel
                        #table
                        #xenon
                        #>>>

#Solution:

file_name = "words.txt"

try:
    handle = open(file_name, "r")
    words = []
    while True:
        content = handle.readline()
        if content == "":
            break
        else:
            words.append(content)
    handle.close()
except IOError:
    print("No such file!")

words.sort()

print("Words in an alphabetical order:")
for i in words:
    print(i)
