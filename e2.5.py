#E2.5-Calculator, taking an input
#Problem:
#Take two numbers from the user with input(),
#calculate the result
#and make the program present the result in the following way:

#Calculator
#Give the first number: 100
#Give the second number: 25
#The result is: 125
#Solution:

print("Calculator")
# Store input numbers
value1 = int(input("Give the first number: "))
value2 = int(input("Give the second number: "))
# Add two numbers
sum = value1 + value2
print("The result is: ",sum)