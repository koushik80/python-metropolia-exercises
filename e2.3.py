#E2.3-Type Conversions
#Problem:
#Start by defining two variables, and assign the first variable the float value 10.6411.
#he second variable gets a string "Stringline!" as a value.
#Convert the first variable to an integer, and multiply the variable with the string by 2.
#After this, finalize the program to print out the results in the following way:
#:Solution:
#Integer conversion cannot do roundings: 10
#Multiplying strings also causes trouble: Stringline!Stringline!


x = 10.6411
y = "Stringline!"

a = int(10.6411)
b = y*2
print("Integer conversion cannot do roundings:",a)
print("Multiplying strings also causes trouble:",b)