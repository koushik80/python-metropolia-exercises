#E2.6
#Problem:
#Define a variable and assign it a string "desserts" as a value.
#Then create three new variables, and assign them values by slicing the
#A) first 4 characters
#B) the last 4 characters and
#C) the entire string backwards as given values.
#Then make the program print the answers in the following way:

#The first 4 characters were: dess
#The last 4 characters were: erts
#The string backwards was: stressed
#Solution:


text = "desserts"
s_1 = text[:4]
s_2 = text[4:]
s_3 = text[::-1]

print("The first 4 characters were: ",s_1)
print("The last 4 characters were: ",s_2)
print("The string backwards was: ",s_3)