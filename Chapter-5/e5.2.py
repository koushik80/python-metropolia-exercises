#E-5.2: Writing to a file
#Problem: Create a program which prompts the user for a file name "Give a file name: "
#and then for an input "Write something: ".
#After this, the program writes the string given by the user to the file
#and reports "Wrote [input] to the file [name].".
#When working correctly, the program prints something like this:

                #>>>
                #Give a file name: log.txt
                #Write something: Attencion, attencion. 10, 10, 22, 33, Adios.
                #Wrote Attencion, attencion. 10, 10, 22, 33, Adios. to the file log.txt.
                #>>>

#Solution:

f_name = str(input("Give a file name: "))
txt = str(input("Write something: "))


f = open(f_name, "w")
f.write(txt)
f.close()
print("Wrote",txt,"to the file",f_name)