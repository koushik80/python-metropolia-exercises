#E-5.1-Reading a file
#Problem:There is a file in the same directory with the exercise source code called "facts.txt", which has a long strip of text.
#Create a program which reads the entire content of the file
#and prints it on the screen with the text "Following was read from the file:".
#When working correctly, the program prints something like this:

#When working correctly, the program prints something like this:
#Proin enim leo, tincidunt eget, sollicitudin a, aliquam sit amet, nisl.
#Proin dapibus tortor eu lectus. Curabitur in risus nec arcu pretium aliquam.
#In hac habitasse platea dictumst. Integer sit amet lacus sit amet pede blandit mattis.
#Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
#Ut odio. Nullam nisl sem, adipiscing id, auctor eu, pulvinar et, nulla.
#Aenean convallis erat. Aliquam iaculis mauris sed sem.

#Fusce ultricies urna sed orci. Suspendisse accumsan ipsum egestas est. Pellentesque nisl.
#Quisque sodales ligula quis mi. In pede sapien, molestie vel, aliquet sit amet, malesuada a, magna. Nulla ipsum.

#Solution:

#Note: There's a seperate file facts.txt in this folder

f = open("facts.txt", "r")
print("Following was read from the file: ",f.read())
